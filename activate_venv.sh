#!/usr/bin/env bash
# Usage: source activate_venv.sh

[ -d .venv ] || python3 -m venv .venv || python -m venv .venv

if [ -f .venv/Scripts/activate ]; then
  source .venv/Scripts/activate   # Windows (Git Bash)
else
  source .venv/bin/activate       # macOS
fi