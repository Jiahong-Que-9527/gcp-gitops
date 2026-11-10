> [房玄龄·2026-11-10] Starter implementation; GCP execution pending.

# Terraform starter: analytics

Independent study root, not an end-to-end platform module. It uses local state
until lab 03 explicitly migrates the backend. No API, project, billing account,
or broad IAM grant is created implicitly.

## Prerequisites

- Existing sandbox, billing, ADC, Terraform 1.14+ and the checked-in provider lock.
- Enable and verify `bigquery.googleapis.com` before a real plan/apply.
- Operator needs: dataset/table management; roles/bigquery.user plus data permissions as needed. Query execution also needs jobs.create.
- Review the region, data location, naming uniqueness and current resource inventory.

## Static verification (no credentials)

```bash
terraform -chdir=infra/stacks/analytics init -backend=false -input=false -lockfile=readonly
terraform -chdir=infra/stacks/analytics validate
```

## Plan after prerequisites

Create a new ignored `local.tfvars` based on `terraform.tfvars.example`, replacing
placeholders with reviewed values. Do not commit the populated local file.

```bash
terraform -chdir=infra/stacks/analytics plan -var-file=local.tfvars
```

No apply/destroy runs in CI. A successful validate does not prove provider IAM,
region availability, quota, deployment health or actual spend. Apply requires
reviewing the concrete target and plan. See [cost/lifecycle](../../../docs/cost-and-lifecycle.md).

## Scope and limitations

One protected table partitioned on event_time and clustered by airport. This is schema scaffolding, not ingestion, quality assertions or durable deduplication.
