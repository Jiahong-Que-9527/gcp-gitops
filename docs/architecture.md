> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Architecture and boundaries

The starting workload validates synthetic aviation events. Reuse one small
domain contract to compare serverless, data, Kubernetes, and AI services.
Real airport data, cargo operations, and private project systems are outside scope.

## Current executable boundary

`samples/events.json` enters the local event API or replay CLI. The shared
contract checks identifiers, UTC-aware timestamps, airport codes, finite
nonnegative delay values, unique event IDs, and `synthetic=true`.
Valid batches return a deterministic aggregate. No database, cloud API, or
external model is called. Requests are not persisted and this is not durable ingestion.

## Target paths, implemented in later labs

1. Serverless: Artifact Registry → authenticated Cloud Run; Secret Manager,
   Cloud Logging, Cloud Monitoring, keyless deployment identity.
2. Data: authenticated producer → Pub/Sub → processing → Storage and BigQuery;
   explicit event IDs, replay, dead-letter handling, data quality and lineage.
3. Kubernetes: Terraform-provisioned GKE → Argo CD → Kustomize workload;
   Git revision, image digest, workload identity, drift, health, recovery.
4. AI: curated synthetic documents/events → Vertex AI evaluation / retrieval;
   repeatable evaluation, prompt-injection tests, latency and per-request cost.

The initial Terraform roots are independent, small study examples. They do not
bootstrap all prerequisites or wire the four paths together. Each root has its
own state; apply only after the lab's prerequisites and plan review.

## Ownership

Terraform owns cloud resources. Argo CD eventually owns its selected workload
resources. CI owns validation/builds. Do not let Terraform and Argo CD manage
the same Kubernetes object, or CI push changes behind the controller's back.
Choose one reconciler per object. Config Sync can be compared later, but should
not reconcile the same manifests as Argo CD.

## Environments

Begin with one sandbox and `dev`. `stage` is introduced only when promotion is
exercised; separate project/IAM/state boundaries are an advanced step. Folders
and namespaces alone do not provide account, billing, or identity isolation.
