> [房玄龄·2026-11-10] Initial observed validation.

# Validation ledger

- WSL: 16 Python/HTTP tests, replay, repository links and prerequisite DAG passed.
- Terraform: four roots fmt/validate, five mocked-provider test runs passed.
- Kubernetes: Kustomize rendered offline; no API server or cluster was contacted.
- Container build/runtime: delegated to initial GitHub CI; local Docker unavailable.
- GCP billing/IAM/APIs, real plan/apply, cloud runtime, and Argo CD sync: not executed.

See [dated local evidence](../evidence/2026-11-10-local-baseline.md). Only lab 00 is
marked local-validated. Later labs remain planned. CI validates scaffolding and
the sample workload; a green check does not demonstrate cloud proficiency.
