> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Cost and resource lifecycle

Start offline. Before creating a resource, record its region, billing owner,
expected lifetime, pricing source, resource label, and approved spend envelope.
No universal cost estimate is hardcoded: prices vary with region and usage.

An alerts-only budget does not cap spending. See [Google's budget documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets).
Scaling Cloud Run to zero does not remove image storage, logs, or other charges.
GKE, VMs/disks, Cloud SQL, Composer, Dataflow, networking, and model endpoints
can incur ongoing charges. Treat them as scheduled, short-lived exercises.

## Before an experiment

- Choose an isolated project; inspect billing and current resource inventory.
- Read the relevant pricing page; define a session duration and expected load.
- Set budget alerts and service-specific quotas/limits where appropriate.
- For BigQuery use a dry run and `maximum_bytes_billed`; LIMIT is not a scan cap.
- Record baseline resources so existing systems are never mistaken for lab assets.

## End-of-session record

Record exact resource IDs, state root/backend, data retention, estimated versus
observed usage, delayed billing caveats, and what remains running. Budget exports
and raw project identifiers should be reviewed before publication.

## Teardown is a separate operation

This repository has no automatic destroy job or project-deletion helper. Before
any deletion, produce a target list and reviewed destroy plan, explain object
counts/data loss/dependencies, preserve state and required data backups, and
obtain explicit approval. Bucket `force_destroy=false`, Cloud Run deletion
protection, and BigQuery dataset-content protection are intentional defaults.
Do not disable protections merely to make a tutorial pass.

Resource labels (`project=gcp-gitops`, `environment=dev`) aid inventory; labels
do not authorize deletion. A snapshot is not automatically an independent backup.
