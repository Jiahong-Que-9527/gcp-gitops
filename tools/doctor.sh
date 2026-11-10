#!/usr/bin/env bash
# [房玄龄·2026-11-10] Report only; do not install or authenticate.
set -eu
printf 'Local baseline (required):\n'
command -v python3
python3 --version
command -v make
printf '\nCloud/container tools (optional until their lab):\n'
for tool in git docker terraform gcloud kubectl; do
  if command -v "$tool"; then :; else printf '%s: not installed\n' "$tool"; fi
done
