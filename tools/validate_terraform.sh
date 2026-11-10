#!/usr/bin/env bash
# [房玄龄·2026-11-10] Provider initialization and static checks only.
set -eu
cd "$(dirname "$0")/.."
terraform fmt -check -recursive infra
for stack in infra/stacks/*; do
  terraform -chdir="$stack" init -backend=false -input=false -lockfile=readonly
  terraform -chdir="$stack" validate
  terraform -chdir="$stack" test
done
