> [房玄龄·2026-11-10] Initial observed validation.

# Validation ledger

- WSL: 16 Python/HTTP tests, replay, repository links and prerequisite DAG passed.
- Terraform: four roots fmt/validate, five mocked-provider test runs passed.
- Kubernetes: Kustomize rendered offline; no API server or cluster was contacted.
- GitHub Actions: [initial Validate run](https://github.com/Jiahong-Que-9527/gcp-gitops/actions/runs/42912796572) passed all four jobs on main
  at `9c708a47b7c7240823a313411a36106823c8849e`. The hosted runner built the
  container, ran it with a read-only filesystem and tested real HTTP responses.
  Local Docker was unavailable; no local engine settings were changed.
- GCP billing/IAM/APIs, real plan/apply, cloud runtime, and Argo CD sync: not executed.

See [dated local evidence](../evidence/2026-11-10-local-baseline.md). Only lab 00 is
marked local-validated. Later labs remain planned. CI validates scaffolding and
the sample workload; a green check does not demonstrate cloud proficiency.
