> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Portfolio: demonstrate engineering judgment

A completed lab is useful when another engineer can reproduce its behavior,
inspect the tradeoffs, and see a recovery attempt. Screenshots supplement
commits, tests, measured outputs, and a short explanation.

## Three final demonstrations

1. **Serverless delivery:** build a versioned artifact, deploy with short-lived
   identity, reject an unauthorized request, observe latency/errors, and restore
   a previous revision. Provide CI run, digest, IAM explanation and cost record.
2. **Event data platform:** ingest synthetic events, handle duplicates and bad
   records, replay a bounded range, transform BigQuery data, and compare query
   scan cost. Provide data contract, quality checks, reconciliation counts and lineage.
3. **GitOps platform / AI workload:** reconcile a digest-pinned service on GKE,
   demonstrate drift recovery and rollback, then serve an evaluated AI feature
   with explicit identity and cost boundaries. Separate platform and model claims.

## Evidence per lab

Use [the template](../evidence/TEMPLATE.md). Include commit SHA, UTC time,
tool versions, redacted commands and outputs, expected versus actual result,
one failure/recovery drill, spend and remaining resources. Publish only reviewed
copies; raw logs/plans/state remain under ignored `artifacts/` or private storage.

Statuses: `planned` (guide only), `local-validated`, `cloud-validated` (functional
cloud checks), `demonstrated` (including negative tests, recovery and evidence).
`catalog.json` is the lab index; changing status requires evidence, not optimism.

## Interview narrative

Explain the problem, chosen design and rejected alternative, how you validated
it, an observed failure, the recovery, and the remaining limitation. Compare
Cloud Run vs GKE; Pub/Sub vs synchronous calls; SQL vs BigQuery; Terraform vs
reconciliation; static keys vs federation; backup vs proven restore.

A future CV bullet may follow: “Built [implemented capability] on [services];
validated [measured result] with [evidence]; documented [cost/recovery boundary].”
Fill this only after execution. Do not claim enterprise scale, production SLOs,
real aviation ground truth, or customer impact from synthetic lab results.
