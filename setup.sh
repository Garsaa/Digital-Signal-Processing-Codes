#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python nao encontrado no PATH. Instale o Python 3.11+ e tente novamente." >&2
  exit 1
fi

"$PYTHON_BIN" "$SCRIPT_DIR/scripts/manage_env.py" setup --system-python "$PYTHON_BIN"

