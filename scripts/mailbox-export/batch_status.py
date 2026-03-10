#!/usr/bin/env python3
"""Check status of batch jobs across all providers. Usage: python batch_status.py"""

from google import genai
from google.genai import types as genai_types
import anthropic

from config import LLM_PROVIDERS

# ── Gemini ──
gemini_cfg = next((p for p in LLM_PROVIDERS if p["provider"] == "gemini"), None)
if gemini_cfg:
    print("GEMINI BATCH JOBS")
    print(f"{'State':<30} {'Created':<20} {'Job Name'}")
    print("-" * 90)
    client = genai.Client(
        api_key=gemini_cfg["api_key"],
        http_options=genai_types.HttpOptions(api_version="v1beta"),
    )
    for job in client.batches.list(config={"page_size": 20}):
        state = getattr(job.state, "name", str(job.state))
        created = job.create_time.strftime("%Y-%m-%d %H:%M") if job.create_time else "?"
        responses = ""
        if job.dest and job.dest.inlined_responses:
            responses = f"  [{len(job.dest.inlined_responses)} responses]"
        print(f"{state:<30} {created:<20} {job.name}{responses}")
    print()

# ── Anthropic ──
anthropic_cfg = next((p for p in LLM_PROVIDERS if p["provider"] == "anthropic"), None)
if anthropic_cfg:
    print("ANTHROPIC BATCH JOBS")
    print(
        f"{'Status':<20} {'Created':<20} {'Succeeded':>10} {'Errored':>10} {'Processing':>10}  {'Batch ID'}"
    )
    print("-" * 110)
    client = anthropic.Anthropic(api_key=anthropic_cfg["api_key"])
    try:
        for batch in client.messages.batches.list(limit=20):
            created = (
                batch.created_at.strftime("%Y-%m-%d %H:%M")
                if hasattr(batch.created_at, "strftime")
                else str(batch.created_at)[:16]
            )
            counts = batch.request_counts
            print(
                f"{batch.processing_status:<20} {created:<20} {counts.succeeded:>10} {counts.errored:>10} {counts.processing:>10}  {batch.id}"
            )
    except Exception as e:
        print(f"  Error listing Anthropic batches: {e}")
    print()
