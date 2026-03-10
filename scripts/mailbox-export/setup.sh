#!/bin/bash
# ═══════════════════════════════════════════════════════════
# setup.sh — Run this once to set up the environment
# ═══════════════════════════════════════════════════════════
set -e

echo "Setting up mailbox-export..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found. Install Python 3.9+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "  Python version: $PYTHON_VERSION"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "  Creating virtual environment..."
    python3 -m venv venv
else
    echo "  Virtual environment already exists."
fi

# Activate and install
source venv/bin/activate
echo "  Installing dependencies..."
pip install --quiet msal requests tqdm google-genai

echo ""
echo "Setup complete!"
echo ""
echo "NEXT STEPS:"
echo "  1. Edit config.py with your credentials"
echo "  2. Run: source venv/bin/activate"
echo "  3. Run: python db.py"
echo "  4. Follow the RUNBOOK.md phases"
echo ""
