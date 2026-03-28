#!/usr/bin/env bash
# Cross-platform Python resolver: python3 (macOS) → python (Windows/miniconda)
if python3 --version >/dev/null 2>&1; then
  exec python3 "$@"
else
  exec python "$@"
fi
