#!/usr/bin/env bash
set -euo pipefail

PY="${PYTHON_BIN:-python}"

$PY -m pip install -U build twine wheel


if [ -d dist ]; then
  rm -rf dist
  echo "deleted dist dir"
else
  echo "dist not found , skipped"
fi


$PY -m build


if [ ! -d dist ] || [ -z "$(ls -A dist)" ]; then
  echo "build failed : dist is empty"
  exit 1
fi


twine check dist/*

if [[ "${1-}" == "--test" ]]; then
  twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
else
  twine upload --skip-existing dist/*
fi
