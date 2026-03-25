#!/usr/bin/env bash
# Serve test fixture HTML forms + mail backend for agent testing.
#
# Starts TWO servers:
#   1. HTTP file server on port 8090 (serves HTML forms)
#   2. Mail backend on port 8091 (receives POST /submit, sends email via SMTP)
#
# Usage: ./serve.sh
#
# Prerequisites:
#   - Copy outreach/.env.example to outreach/.env and fill in SMTP credentials
#
# Forms available at:
#   http://localhost:8090/simple-form.html
#   http://localhost:8090/multi-field-form.html
#   http://localhost:8090/captcha-form.html

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
HTTP_PORT=8090
MAIL_PORT=8091

# Check for .env
# Check for .env in project root
ENV_FILE="$DIR/../../.env"
if [ ! -f "$ENV_FILE" ]; then
    echo "WARNING: Project root .env not found at $ENV_FILE"
    echo "  SMTP credentials (SMTP_HOST, SMTP_USER, SMTP_PASSWORD, etc.) must be in .env"
    echo "  Forms will load but email sending will fail."
    echo ""
fi

cleanup() {
    echo ""
    echo "Stopping servers..."
    kill "$HTTP_PID" "$MAIL_PID" 2>/dev/null || true
    wait "$HTTP_PID" "$MAIL_PID" 2>/dev/null || true
    echo "Done."
}
trap cleanup EXIT INT TERM

# Start mail backend
echo "Starting mail backend on http://localhost:$MAIL_PORT ..."
python3 "$DIR/mail-server.py" --port "$MAIL_PORT" &
MAIL_PID=$!
sleep 1

# Start HTTP file server
echo "Starting HTTP server on http://localhost:$HTTP_PORT ..."
python3 -m http.server "$HTTP_PORT" --directory "$DIR" 2>/dev/null &
HTTP_PID=$!

echo ""
echo "══════════════════════════════════════════════════"
echo "  OUTREACH TEST FIXTURES RUNNING"
echo "══════════════════════════════════════════════════"
echo "  Forms:"
echo "    simple-form.html       → http://localhost:$HTTP_PORT/simple-form.html"
echo "    multi-field-form.html  → http://localhost:$HTTP_PORT/multi-field-form.html"
echo "    captcha-form.html      → http://localhost:$HTTP_PORT/captcha-form.html"
echo ""
echo "  Mail backend:  http://localhost:$MAIL_PORT/submit"
echo "══════════════════════════════════════════════════"
echo ""
echo "Press Ctrl+C to stop both servers."
echo ""

# Wait for either to exit
wait -n "$HTTP_PID" "$MAIL_PID" 2>/dev/null || true
