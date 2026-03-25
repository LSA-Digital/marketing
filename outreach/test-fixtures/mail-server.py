#!/usr/bin/env python3
"""
Lightweight HTTP backend for outreach test fixture forms.
Accepts POST /submit with form data, sends email via SMTP, returns JSON.

SMTP config loaded from outreach/.env (relative to this script's parent dir).

Usage:
    python3 mail-server.py [--port 8091]
"""

import json
import os
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from pathlib import Path
from datetime import datetime, timezone


def load_env(env_path):
    """Load .env file into os.environ. Handles quotes and comments."""
    if not env_path.exists():
        print(f"WARNING: {env_path} not found. Email sending will fail.")
        print(f"Copy .env.example to .env and fill in SMTP credentials.")
        return

    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("'\"")
            os.environ.setdefault(key, value)


def send_email(form_data, source_form):
    """Send an email with the submitted form data via SMTP."""
    smtp_host = os.environ.get("SMTP_HOST", "")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER", "")
    smtp_pass = os.environ.get("SMTP_PASSWORD", "")
    smtp_from = os.environ.get("SMTP_FROM", smtp_user)
    smtp_to = os.environ.get("SMTP_TO", smtp_from)  # default: send to self
    use_tls = os.environ.get("SMTP_USE_TLS", "true").lower() in ("true", "1", "yes")

    if not all([smtp_host, smtp_user, smtp_pass]):
        return {
            "success": False,
            "error": "SMTP not configured. Set SMTP_HOST, SMTP_USER, SMTP_PASSWORD in project root .env",
        }

    # Build email
    msg = MIMEMultipart("alternative")
    msg["From"] = smtp_from
    msg["To"] = smtp_to
    msg["Subject"] = f"[Outreach Test] Form submission from {source_form}"

    # Plain text body
    lines = [
        f"Contact form submission received at {datetime.now(timezone.utc).isoformat()}",
        f"Source form: {source_form}",
        "",
        "--- Form Data ---",
    ]
    for key, values in form_data.items():
        val = values[0] if isinstance(values, list) else values
        lines.append(f"{key}: {val}")

    plain_body = "\n".join(lines)

    # HTML body
    rows = ""
    for key, values in form_data.items():
        val = values[0] if isinstance(values, list) else values
        rows += f"<tr><td style='padding:6px 12px;font-weight:600;vertical-align:top;border-bottom:1px solid #eee'>{key}</td><td style='padding:6px 12px;border-bottom:1px solid #eee'>{val}</td></tr>"

    html_body = f"""<html><body style="font-family:-apple-system,sans-serif;color:#333">
    <h2 style="color:#1a5276">Contact Form Submission</h2>
    <p><strong>Source:</strong> {source_form}<br>
    <strong>Time:</strong> {datetime.now(timezone.utc).isoformat()}</p>
    <table style="border-collapse:collapse;width:100%;max-width:600px">{rows}</table>
    <hr style="margin-top:24px;border:none;border-top:1px solid #ddd">
    <p style="font-size:12px;color:#999">Sent by outreach test fixture mail-server.py</p>
    </body></html>"""

    msg.attach(MIMEText(plain_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            if use_tls:
                server.starttls()
                server.ehlo()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_from, smtp_to, msg.as_string())
        return {"success": True, "to": smtp_to}
    except Exception as e:
        return {"success": False, "error": str(e)}


class FormHandler(BaseHTTPRequestHandler):
    """Handles POST /submit from test fixture forms."""

    def do_POST(self):
        if self.path != "/submit":
            self.send_error(404, "Not Found")
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        content_type = self.headers.get("Content-Type", "")

        # Parse form data
        if "application/x-www-form-urlencoded" in content_type:
            form_data = parse_qs(body)
        elif "application/json" in content_type:
            raw = json.loads(body)
            form_data = {
                k: [v] if not isinstance(v, list) else v for k, v in raw.items()
            }
        else:
            self.send_error(400, f"Unsupported Content-Type: {content_type}")
            return

        # Extract source form identifier from Referer header
        referer = self.headers.get("Referer", "unknown-form")
        source_form = referer.split("/")[-1] if "/" in referer else referer

        # Send email
        result = send_email(form_data, source_form)

        # Respond with JSON
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode("utf-8"))

        status = "OK" if result["success"] else f"FAIL: {result.get('error', '?')}"
        print(f"  [{source_form}] → {status}")

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        """Suppress default logging — we log manually."""
        pass


def main():
    port = 8091
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--port" and i < len(sys.argv) - 1:
            port = int(sys.argv[i + 1])

    # Load .env from project root
    script_dir = Path(__file__).resolve().parent
    env_path = script_dir.parent.parent / ".env"  # outreach/test-fixtures -> outreach -> project root
    load_env(env_path)

    print(f"Mail server listening on http://localhost:{port}")
    print(
        f"  POST /submit → sends email via {os.environ.get('SMTP_HOST', '(not configured)')}"
    )
    print(f"  SMTP_FROM: {os.environ.get('SMTP_FROM', '(not configured)')}")
    print(f"  .env: {env_path}")
    print()

    server = HTTPServer(("", port), FormHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nMail server stopped.")
        server.server_close()


if __name__ == "__main__":
    main()
