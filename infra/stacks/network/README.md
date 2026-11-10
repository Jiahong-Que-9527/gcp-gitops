> [房玄龄·2026-11-10] Starter implementation; GCP execution pending.

# Terraform starter: network

Independent study root, not an end-to-end platform module. It uses local state
until lab 03 explicitly migrates the backend. No API, project, billing account,
or broad IAM grant is created implicitly.

## Prerequisites

- Existing sandbox, billing, ADC, Terraform 1.14+ and the checked-in provider lock.
- Enable and verify `compute.googleapis.com` before a real plan/apply.
- Operator needs: network/subnetwork management; e.g. roles/compute.networkAdmin for the bootstrap identity, not application runtime.
- Review the region, data location, naming uniqueness and current resource inventory.

## Static verification (no credentials)

```bash
terraform -chdir=infra/stacks/network init -backend=false -input=false -lockfile=readonly
terraform -chdir=infra/stacks/network validate
```

## Plan after prerequisites

Create a new ignored `local.tfvars` based on `terraform.tfvars.example`, replacing
placeholders with reviewed values. Do not commit the populated local file.

```bash
terraform -chdir=infra/stacks/network plan -var-file=local.tfvars
```

No apply/destroy runs in CI. A successful validate does not prove provider IAM,
region availability, quota, deployment health or actual spend. Apply requires
reviewing the concrete target and plan. See [cost/lifecycle](../../../docs/cost-and-lifecycle.md).

## Scope and limitations

One custom VPC/subnet, no VMs, NAT, public ingress rules, or cluster secondary ranges. Private Google Access does not supply general internet egress.
