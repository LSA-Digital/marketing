#!/usr/bin/env python3
"""
PASS 2: Classify every unclassified message using LLM Batch APIs.

Supports multiple providers with automatic fallback (configured in config.py):
  - Google Gemini (Batch API via google-genai SDK)
  - Anthropic Claude (Message Batches API via anthropic SDK)

Providers are tried in order. If one returns 429 (quota exhausted),
the script falls back to the next provider for remaining emails.

Each email = 1 request. State persisted to .batch_state.json for resume.
"""

import sys
import json
import time
from datetime import datetime
from pathlib import Path

from google import genai
from google.genai import types as genai_types
import anthropic

from config import LLM_PROVIDERS, TAG_DEFINITIONS, ORG_DOMAINS
from db import get_db, set_classification, get_stats


# ── Logging ──

LOG_FILE = Path(__file__).parent / "pass2_classify.log"
STATE_FILE = Path(__file__).parent / ".batch_state.json"
_log_fh = None


def log(msg: str = ""):
    """Print to console AND append to log file with timestamp."""
    global _log_fh
    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    if _log_fh is None:
        _log_fh = open(LOG_FILE, "a")
    _log_fh.write(line + "\n")
    _log_fh.flush()


# ── State persistence ──


def save_state(jobs):
    """Save active batch jobs — list of {provider, job_name, msg_ids, submitted_at}."""
    STATE_FILE.write_text(json.dumps({"jobs": jobs}))


def load_state():
    """Load saved batch state, or None if no active batches."""
    if not STATE_FILE.exists():
        return None
    try:
        data = json.loads(STATE_FILE.read_text())
        # Migrate old format: add provider field if missing
        if "job_name" in data:
            data = {
                "jobs": [
                    {
                        "provider": "gemini",
                        "job_name": data["job_name"],
                        "msg_ids": data["msg_ids"],
                        "submitted_at": data["submitted_at"],
                    }
                ]
            }
        for job in data.get("jobs", []):
            if "provider" not in job:
                job["provider"] = "gemini"
        return data
    except (json.JSONDecodeError, KeyError):
        STATE_FILE.unlink(missing_ok=True)
        return None


def clear_state():
    """Remove state file after results are extracted."""
    STATE_FILE.unlink(missing_ok=True)


# ── System prompt & email formatting (provider-agnostic) ──

SYSTEM_PROMPT = f"""You are an email classification system for a digital services
company (LSA Digital). You are processing emails from shared mailboxes.

For each email, you must decide:
1. ACTION: KEEP, SPAM, or NEWSLETTER
   - KEEP: legitimate business email worth retaining
   - SPAM: unsolicited junk, phishing, scams, irrelevant marketing
   - NEWSLETTER: mailing lists, digests, automated marketing campaigns,
     promotional emails, event invitations from marketing platforms

2. TAGS: Apply ALL tags that match (can be zero or many):
{TAG_DEFINITIONS}

IMPORTANT RULES:
- Emails from these org domains are ALWAYS action=KEEP: {", ".join(ORG_DOMAINS)}
- Having a List-Unsubscribe header strongly suggests NEWSLETTER
- "noreply@" senders that are transactional (order confirmations, password resets)
  should be KEEP if from a legitimate service the company uses
- Government emails (.gov, .mil) are always KEEP and tagged GOV
- When in doubt between SPAM and NEWSLETTER, choose NEWSLETTER
- When in doubt between NEWSLETTER and KEEP, choose KEEP

Respond with a JSON object (NOT an array) with:
  - "action": "KEEP" | "SPAM" | "NEWSLETTER"
  - "confidence": 0.0 to 1.0
  - "reason": brief explanation (1 sentence)
  - "tags": array of tag objects, each with "tag", "confidence", "reason"
"""

POLL_INTERVAL = 10  # seconds between status checks
POLL_TIMEOUT = 7200  # max seconds to wait (2 hours)


def format_email(row):
    """Format a single DB row into the prompt text for classification."""
    return json.dumps(
        {
            "mailbox": row["mailbox_name"],
            "sender": f"{row['sender_name']} <{row['sender_address']}>",
            "to": row["to_recipients"],
            "subject": row["subject"] or "(no subject)",
            "date": row["received_at"],
            "importance": row["importance"],
            "has_attachments": bool(row["has_attachments"]),
            "has_list_headers": bool(row["has_list_headers"]),
            "list_headers": row["list_header_names"] or "[]",
        }
    )


def parse_classification(text, msg_id):
    """Parse JSON classification from LLM response text. Returns (result, error)."""
    try:
        result = json.loads(text)
        return result, None
    except json.JSONDecodeError as e:
        return None, f"JSON error (msg_id={msg_id}): {e}"


def save_classification(db, msg_id, result):
    """Write parsed classification result to DB."""
    set_classification(
        db,
        message_id=msg_id,
        action=result.get("action", "KEEP"),
        reason=result.get("reason", ""),
        confidence=result.get("confidence", 0.5),
        tags=result.get("tags", []),
    )


# ═══════════════════════════════════════════════════════════════
# PROVIDER: GEMINI
# ═══════════════════════════════════════════════════════════════


def init_gemini(provider_cfg):
    """Initialize Gemini client."""
    return genai.Client(
        api_key=provider_cfg["api_key"],
        http_options=genai_types.HttpOptions(api_version="v1beta"),
    )


def submit_gemini_batches(client, rows, provider_cfg):
    """Submit rows as Gemini batch jobs. Returns list of job infos."""
    model = provider_cfg["model"]
    max_per_batch = provider_cfg.get("batch_size", 1000)
    all_jobs = []
    total = len(rows)
    total_chunks = (total + max_per_batch - 1) // max_per_batch

    for chunk_start in range(0, total, max_per_batch):
        chunk_end = min(chunk_start + max_per_batch, total)
        chunk_rows = rows[chunk_start:chunk_end]
        chunk_num = (chunk_start // max_per_batch) + 1

        log(
            f"  Building Gemini batch {chunk_num}/{total_chunks}: {len(chunk_rows)} emails..."
        )

        # Build InlinedRequests
        requests = []
        for row in chunk_rows:
            email_text = format_email(row)
            requests.append(
                {
                    "contents": [
                        {
                            "parts": [
                                {"text": f"Classify this email:\n\n{email_text}"}
                            ],
                            "role": "user",
                        }
                    ],
                    "metadata": {"msg_id": str(row["id"])},
                    "config": {
                        "system_instruction": SYSTEM_PROMPT,
                        "response_mime_type": "application/json",
                        "temperature": 0.1,
                        "max_output_tokens": 512,
                    },
                }
            )

        log(f"  Submitting to {model}...")
        try:
            batch_job = client.batches.create(
                model=model,
                src=requests,
                config={
                    "display_name": f"mailbox-classify-{chunk_num}-{int(time.time())}"
                },
            )
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                log(f"  QUOTA EXHAUSTED on batch {chunk_num}/{total_chunks}")
                return all_jobs, "quota_exhausted"
            log(f"  SUBMIT FAILED: {e}")
            log(f"  Waiting 10s before next batch...")
            time.sleep(10)
            continue

        job_info = {
            "provider": "gemini",
            "job_name": batch_job.name,
            "msg_ids": [row["id"] for row in chunk_rows],
            "submitted_at": datetime.now().isoformat(),
        }
        all_jobs.append(job_info)
        log(
            f"  Submitted: {batch_job.name} ({getattr(batch_job.state, 'name', batch_job.state)})"
        )

        if chunk_num < total_chunks:
            log(f"  Waiting 5s before next batch...")
            time.sleep(5)

    return all_jobs, None


def poll_gemini_jobs(client, jobs, db):
    """Poll Gemini batch jobs until all complete. Returns (classified, errors)."""
    if not jobs:
        return 0, 0

    log(f"  Polling {len(jobs)} Gemini batch job(s) every {POLL_INTERVAL}s...")
    start = time.time()
    total_classified = 0
    total_errors = 0
    pending = list(jobs)
    last_states = {}

    while pending:
        still_pending = []
        for job_info in pending:
            job_name = job_info["job_name"]
            job = client.batches.get(name=job_name)
            job_state = getattr(job.state, "name", str(job.state))

            if job_state != last_states.get(job_name):
                log(f"  {job_name}: {job_state}")
                last_states[job_name] = job_state

            if not job.done:
                still_pending.append(job_info)
                continue

            # Done — extract results
            if job_state in ("JOB_STATE_SUCCEEDED", "JOB_STATE_PARTIALLY_SUCCEEDED"):
                classified, errors = collect_gemini_results(job, db)
                total_classified += classified
                total_errors += errors
                log(f"    Extracted: {classified} classified, {errors} errors")
            else:
                log(f"    Failed: {job.error}")

        pending = still_pending

        if pending:
            save_state(pending)
            elapsed = time.time() - start
            if elapsed > POLL_TIMEOUT:
                log(
                    f"  TIMEOUT after {elapsed:.0f}s — {len(pending)} jobs still running"
                )
                return total_classified, total_errors
            time.sleep(POLL_INTERVAL)
        else:
            clear_state()

    return total_classified, total_errors


def collect_gemini_results(job, db):
    """Extract classifications from a completed Gemini batch job."""
    if not job.dest or not job.dest.inlined_responses:
        log("  ERROR: No inlined_responses in batch result")
        return 0, 0

    classified = 0
    errors = 0

    for resp in job.dest.inlined_responses:
        msg_id = int(resp.metadata.get("msg_id", 0)) if resp.metadata else 0

        if resp.error:
            log(f"  Item error (msg_id={msg_id}): {resp.error}")
            errors += 1
            continue

        if not resp.response or not resp.response.text:
            log(f"  Empty response (msg_id={msg_id})")
            errors += 1
            continue

        result, err = parse_classification(resp.response.text, msg_id)
        if err:
            log(f"  {err}")
            errors += 1
        else:
            save_classification(db, msg_id, result)
            classified += 1

    return classified, errors


# ═══════════════════════════════════════════════════════════════
# PROVIDER: ANTHROPIC
# ═══════════════════════════════════════════════════════════════


def init_anthropic(provider_cfg):
    """Initialize Anthropic client."""
    return anthropic.Anthropic(api_key=provider_cfg["api_key"])


def submit_anthropic_batches(client, rows, provider_cfg):
    """Submit rows as Anthropic message batches. Returns list of job infos."""
    model = provider_cfg["model"]
    max_per_batch = provider_cfg.get("batch_size", 10000)
    all_jobs = []
    total = len(rows)
    total_chunks = (total + max_per_batch - 1) // max_per_batch

    for chunk_start in range(0, total, max_per_batch):
        chunk_end = min(chunk_start + max_per_batch, total)
        chunk_rows = rows[chunk_start:chunk_end]
        chunk_num = (chunk_start // max_per_batch) + 1

        log(
            f"  Building Anthropic batch {chunk_num}/{total_chunks}: {len(chunk_rows)} emails..."
        )

        # Build batch requests
        requests = []
        for row in chunk_rows:
            email_text = format_email(row)
            requests.append(
                {
                    "custom_id": str(row["id"]),
                    "params": {
                        "model": model,
                        "max_tokens": 512,
                        "temperature": 0.1,
                        "system": SYSTEM_PROMPT,
                        "messages": [
                            {
                                "role": "user",
                                "content": f"Classify this email:\n\n{email_text}",
                            }
                        ],
                    },
                }
            )

        log(f"  Submitting to {model}...")
        try:
            batch = client.messages.batches.create(requests=requests)
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "rate" in err_str.lower():
                log(f"  QUOTA EXHAUSTED on batch {chunk_num}/{total_chunks}")
                return all_jobs, "quota_exhausted"
            log(f"  SUBMIT FAILED: {e}")
            log(f"  Waiting 10s before next batch...")
            time.sleep(10)
            continue

        job_info = {
            "provider": "anthropic",
            "job_name": batch.id,
            "msg_ids": [row["id"] for row in chunk_rows],
            "submitted_at": datetime.now().isoformat(),
        }
        all_jobs.append(job_info)
        log(f"  Submitted: {batch.id} (processing_status={batch.processing_status})")

        if chunk_num < total_chunks:
            log(f"  Waiting 5s before next batch...")
            time.sleep(5)

    return all_jobs, None


def poll_anthropic_jobs(client, jobs, db):
    """Poll Anthropic batch jobs until all complete. Returns (classified, errors)."""
    if not jobs:
        return 0, 0

    log(f"  Polling {len(jobs)} Anthropic batch job(s) every {POLL_INTERVAL}s...")
    start = time.time()
    total_classified = 0
    total_errors = 0
    pending = list(jobs)
    last_states = {}

    while pending:
        still_pending = []
        for job_info in pending:
            batch_id = job_info["job_name"]
            status = client.messages.batches.retrieve(batch_id)
            state = status.processing_status

            if state != last_states.get(batch_id):
                counts = status.request_counts
                log(
                    f"  {batch_id}: {state} "
                    f"(succeeded={counts.succeeded} errored={counts.errored} "
                    f"processing={counts.processing})"
                )
                last_states[batch_id] = state

            if state != "ended":
                still_pending.append(job_info)
                continue

            # Done — stream results
            classified, errors = collect_anthropic_results(client, batch_id, db)
            total_classified += classified
            total_errors += errors
            log(f"    Extracted: {classified} classified, {errors} errors")

        pending = still_pending

        if pending:
            save_state(pending)
            elapsed = time.time() - start
            if elapsed > POLL_TIMEOUT:
                log(
                    f"  TIMEOUT after {elapsed:.0f}s — {len(pending)} jobs still running"
                )
                return total_classified, total_errors
            time.sleep(POLL_INTERVAL)
        else:
            clear_state()

    return total_classified, total_errors


def collect_anthropic_results(client, batch_id, db):
    """Stream and process results from a completed Anthropic batch."""
    classified = 0
    errors = 0

    for entry in client.messages.batches.results(batch_id):
        msg_id = int(entry.custom_id)

        if entry.result.type == "errored":
            log(f"  Item error (msg_id={msg_id}): {entry.result.error}")
            errors += 1
            continue

        if entry.result.type in ("expired", "canceled"):
            log(f"  Item {entry.result.type} (msg_id={msg_id})")
            errors += 1
            continue

        # Succeeded
        text = entry.result.message.content[0].text
        result, err = parse_classification(text, msg_id)
        if err:
            log(f"  {err}")
            errors += 1
        else:
            save_classification(db, msg_id, result)
            classified += 1

    return classified, errors


# ═══════════════════════════════════════════════════════════════
# PROVIDER DISPATCH
# ═══════════════════════════════════════════════════════════════


PROVIDER_FUNCS = {
    "gemini": {
        "init": init_gemini,
        "submit": submit_gemini_batches,
        "poll": poll_gemini_jobs,
    },
    "anthropic": {
        "init": init_anthropic,
        "submit": submit_anthropic_batches,
        "poll": poll_anthropic_jobs,
    },
}


def get_client(provider_cfg):
    """Initialize and return client for a provider."""
    provider = provider_cfg["provider"]
    return PROVIDER_FUNCS[provider]["init"](provider_cfg)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════


def main():
    start_time = datetime.now()

    providers_str = " → ".join(p["provider"] + ":" + p["model"] for p in LLM_PROVIDERS)
    log("=" * 60)
    log("PASS 2: LLM Classification (Multi-Provider Batch API)")
    log(f"  Providers: {providers_str}")
    log(f"  Log file: {LOG_FILE}")
    log("=" * 60)

    db = get_db()
    total_classified = 0
    total_errors = 0

    # Phase 1: Collect results from any previously submitted batch jobs
    state = load_state()
    if state and state.get("jobs"):
        log(f"  Found {len(state['jobs'])} active batch job(s) — checking status...")

        # Group jobs by provider
        by_provider = {}
        for job_info in state["jobs"]:
            p = job_info.get("provider", "gemini")
            by_provider.setdefault(p, []).append(job_info)

        remaining_all = []
        for provider_name, jobs in by_provider.items():
            # Find matching provider config
            provider_cfg = next(
                (p for p in LLM_PROVIDERS if p["provider"] == provider_name), None
            )
            if not provider_cfg:
                log(
                    f"  WARNING: No config for provider '{provider_name}' — skipping {len(jobs)} jobs"
                )
                remaining_all.extend(jobs)
                continue

            client = get_client(provider_cfg)
            funcs = PROVIDER_FUNCS[provider_name]

            # Check each job
            for job_info in jobs:
                job_name = job_info["job_name"]
                try:
                    if provider_name == "gemini":
                        job = client.batches.get(name=job_name)
                        done = job.done
                        job_state = getattr(job.state, "name", str(job.state))
                    else:
                        status = client.messages.batches.retrieve(job_name)
                        done = status.processing_status == "ended"
                        job_state = status.processing_status
                except Exception as e:
                    log(f"  Error checking {job_name}: {e}")
                    remaining_all.append(job_info)
                    continue

                if not done:
                    log(
                        f"  {job_name}: {job_state} ({len(job_info['msg_ids'])} emails)"
                    )
                    remaining_all.append(job_info)
                    continue

                log(f"  {job_name}: {job_state}")
                if provider_name == "gemini":
                    if job_state in (
                        "JOB_STATE_SUCCEEDED",
                        "JOB_STATE_PARTIALLY_SUCCEEDED",
                    ):
                        classified, errors = collect_gemini_results(job, db)
                        total_classified += classified
                        total_errors += errors
                        log(f"    Extracted: {classified} classified, {errors} errors")
                    else:
                        log(f"    Failed: {job.error}")
                else:
                    classified, errors = collect_anthropic_results(client, job_name, db)
                    total_classified += classified
                    total_errors += errors
                    log(f"    Extracted: {classified} classified, {errors} errors")

        if remaining_all:
            save_state(remaining_all)
        else:
            clear_state()
        state = load_state()

    # Phase 2: Query unclassified messages
    rows = db.execute("""
        SELECT m.id, m.graph_id, m.subject, m.sender_address, m.sender_name,
               m.to_recipients, m.received_at, m.importance, m.has_attachments,
               m.has_list_headers, m.list_header_names,
               mb.email as mailbox_email, mb.display_name as mailbox_name
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        WHERE m.action IS NULL
        ORDER BY m.received_at DESC
    """).fetchall()

    log(f"  Unclassified messages: {len(rows)}")

    # Phase 3: Submit to providers with fallback
    active_jobs = state["jobs"] if state and state.get("jobs") else []

    if rows:
        remaining_rows = rows
        for provider_cfg in LLM_PROVIDERS:
            if not remaining_rows:
                break

            provider = provider_cfg["provider"]
            model = provider_cfg["model"]
            log(f"  Trying {provider}:{model} for {len(remaining_rows)} emails...")

            client = get_client(provider_cfg)
            funcs = PROVIDER_FUNCS[provider]

            new_jobs, status = funcs["submit"](client, remaining_rows, provider_cfg)
            active_jobs.extend(new_jobs)

            if new_jobs:
                save_state(active_jobs)
                # Count how many emails were successfully submitted
                submitted_ids = set()
                for j in new_jobs:
                    submitted_ids.update(j["msg_ids"])
                remaining_rows = [
                    r for r in remaining_rows if r["id"] not in submitted_ids
                ]
                log(
                    f"  {provider}: submitted {len(submitted_ids)} emails in {len(new_jobs)} batch(es)"
                )

            if status == "quota_exhausted" and remaining_rows:
                log(
                    f"  {provider} quota exhausted — {len(remaining_rows)} emails remaining, trying next provider..."
                )
                continue
            elif status == "quota_exhausted":
                log(f"  {provider} quota exhausted but all emails submitted.")
                break
            else:
                break  # Success or non-quota error

        if remaining_rows:
            log(
                f"  WARNING: {len(remaining_rows)} emails could not be submitted to any provider"
            )

        log(f"  Total active jobs: {len(active_jobs)}")

    elif not active_jobs:
        log("  Nothing to classify.")
        if total_classified:
            log("")
            log("Results:")
            get_stats(db)
        db.close()
        return

    # Phase 4: Poll ALL jobs until complete
    if active_jobs:
        log("")
        # Group by provider for polling
        by_provider = {}
        for job_info in active_jobs:
            p = job_info.get("provider", "gemini")
            by_provider.setdefault(p, []).append(job_info)

        for provider_name, jobs in by_provider.items():
            provider_cfg = next(
                (p for p in LLM_PROVIDERS if p["provider"] == provider_name), None
            )
            if not provider_cfg:
                log(f"  No config for provider '{provider_name}' — cannot poll")
                continue

            client = get_client(provider_cfg)
            funcs = PROVIDER_FUNCS[provider_name]
            classified, errors = funcs["poll"](client, jobs, db)
            total_classified += classified
            total_errors += errors

    elapsed = (datetime.now() - start_time).total_seconds()

    log("")
    log("=" * 60)
    log("CLASSIFICATION COMPLETE")
    log(f"  Classified: {total_classified}  |  Per-item errors: {total_errors}")
    log(
        f"  Wall time: {elapsed:.1f}s  ({total_classified / max(elapsed, 0.1):.1f} emails/sec)"
    )
    log("")
    log("Results:")
    get_stats(db)
    log("")
    log("Next: python pass3_outlook_sync.py")
    log("=" * 60)
    if _log_fh:
        _log_fh.close()
    db.close()


if __name__ == "__main__":
    main()
