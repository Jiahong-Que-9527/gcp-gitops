> [房玄龄·2026-11-10] Observed initial local verification.

# Initial local baseline

- Status: local-validated. GCP deployment and GitOps reconciliation are not executed.
- Author: Codex / 房玄龄, on behalf of Jiahong Que.
- Execution: WSL Ubuntu on x86_64, Python 3.14.4.
- Timestamp: 2026-11-10T22:14:40.467363+00:00.
- Reproduce from the commit that introduces this note: make check, make replay,
  make terraform-check, and the Kustomize render command below.

## Observed results

- make check: 16 Python unit / actual loopback HTTP tests passed. These include
  positive aggregation, malformed JSON, strict field values, within-batch duplicates,
  missing timezone, huge/nonfinite delay values, invalid media type and body bounds.
- make replay: {"accepted": 3, "mean_delay_minutes": 5.0, "synthetic": true}.
- tools/check_repo.py: 33 lab IDs, prerequisite DAG, evidence paths and Markdown
  link targets checked. The checker was corrected after a regex warning and rerun.
- Terraform 1.14.0, hashicorp/google 7.30.0: four roots passed fmt/validate.
  Five terraform test runs passed with a **mock provider**, including private
  Storage defaults, protected partitioned BigQuery table, explicit private subnet,
  scale-bounded Cloud Run config and rejection of mutable image tags.
- kubectl v1.34.2 / Kustomize v5.7.1:
  kubectl kustomize gitops/workloads/event-api/overlays/dev rendered successfully.
  This is render validation, not Kubernetes admission, scheduling or rollout.

## Failures and limitations

The local Docker engine was unavailable. Windows Docker Desktop's Linux-engine
pipe was absent and Ubuntu's Docker integration was inactive. No Docker settings
were changed. A credential-free GitHub CI job will build the image and exercise
real container HTTP health, valid batch and invalid batch responses; its result
will be recorded separately.

No gcloud installation/login, GCP project discovery, billing changes, IAM grants,
Terraform real-cloud plan/apply, cloud request, or cluster/controller installation
was performed. The workload image in GitOps remains a deliberate placeholder.
Most lab guides are staged implementation tasks, not completed integrations.

## Recovery, cost and retained artifacts

Invalid requests are rejected and subsequent valid HTTP requests pass. No test
data is persisted by the API. No GCP resources or charges were introduced by
these local checks. GitHub CI compute is subject to the account's current plan.

Repo-local validation binaries, their checksum files, provider caches and rendered
output are ignored in .tools/, .terraform/ and artifacts/. Initial README
backup is outside the repository at /home/bill/backups/gcp-gitops-2026-11-10/.
No deletion or automatic cleanup was performed.

Next: lab 01's project, identity and billing preparation, then lab 02's first
cloud plan. Cloud practice requires selecting and authorizing the actual target.
