#!/usr/bin/env bash
# Run the backend in development using the project's virtualenv
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

if [ -f ".venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

export FLASK_ENV=development

# load .env if present
if [ -f .env ]; then
  # shellcheck disable=SC1091
  set -o allexport
  source .env
  set +o allexport
fi

echo "Starting backend (FLASK_ENV=$FLASK_ENV)"
python main.py
