> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# GCP GitOps Engineering Lab

[![Validate](https://github.com/Jiahong-Que-9527/gcp-gitops/actions/workflows/validate.yml/badge.svg)](https://github.com/Jiahong-Que-9527/gcp-gitops/actions/workflows/validate.yml)

A personal, progressive Google Cloud engineering lab for building practical
Data / AI Platform Engineering skills and an evidence-backed portfolio.
Start locally, deploy a small serverless service, build a data pipeline,
then operate Kubernetes with GitOps. Learn to explain the cost, permissions,
failure modes, and recovery of each system.

**Current scope:** runnable local Python service and synthetic event contract;
four Terraform starter stacks; a Kubernetes workload and manual-sync Argo CD
application; 33 sequenced lab guides. Cloud resources have not been deployed
or validated by this initial setup. Later guides are implementation briefs,
not completed integrations. [Validation record](docs/validation.md).

## Start here · Guided FX data pipeline course

<!-- [房玄龄·2026-11-11] Guided FX course entry. -->

[从一份 CSV 开始学数据管道](course/README.md) is the guided learning path.
Start with [Lesson 1](course/01-read-csv.md), then follow the lessons on Python
tests and SQL. The first three lessons use synthetic data and Python's standard
library. Each lesson includes runnable steps, expected output and an exercise.
[Lesson 4.1](course/04-01-fetch-ecb-usd.md) connects the same exercises to live ECB data.

```bash
python3 -m course.fx_csv course/fixtures/rates.csv
# accepted=2, rejected=1
# line 4: fx_rate must be a decimal number
```

## Aviation event API quickstart

```bash
git clone https://github.com/Jiahong-Que-9527/gcp-gitops.git
cd gcp-gitops
make check
make run
# In a second terminal:
curl --fail http://127.0.0.1:8080/healthz
curl --fail -H 'Content-Type: application/json' \
  --data-binary @samples/events.json http://127.0.0.1:8080/validate
```

Python 3.11+ and make are sufficient for the local baseline; no Google account
or third-party Python packages are needed. To exercise the offline data path:

```bash
python3 tools/replay.py samples/events.json
```

- [中文开始指南](docs/getting-started.zh-CN.md)
- [由易到难的路线与练习索引](docs/roadmap.zh-CN.md)
- [Cost and resource lifecycle](docs/cost-and-lifecycle.md)
- [Portfolio and interview evidence](docs/portfolio.md)
- [Architecture and boundaries](docs/architecture.md)
- [Official references](docs/references.md)

## Learning outcomes

1. Operate a dedicated sandbox with explicit identity, budget, and resource ownership.
2. Provision infrastructure using Terraform; review plans and recover state.
3. Package and deploy an authenticated Cloud Run service with keyless CI identity.
4. Deliver and replay synthetic events through Pub/Sub, Storage, and BigQuery.
5. Reconcile GKE workloads from Git, investigate drift, and roll back changes.
6. Measure reliability, access control, data quality, performance, and cost.
7. Extend the platform with evaluated AI workloads and documented tradeoffs.

The curriculum covers common job-relevant GCP capabilities. It does not claim
every Google Cloud product, enterprise production operation, or airport ground
truth. The sample aviation records are deliberately synthetic engineering data.

## Repository map

- `course/`: guided FX lessons, local fixtures and SQL exercises.
- `labs/`: individual guides with prerequisites, tasks, failure drills, and acceptance evidence.
- `apps/event-api/`: dependency-free reference service and container build context.
- `infra/stacks/`: independent Terraform roots for Storage, VPC, BigQuery, and Cloud Run.
- `gitops/`: Kubernetes workload and Argo CD bootstrap example, not installed automatically.
- `samples/`: synthetic data and a BigQuery query example.
- `tests/`, `tools/`: behavioral tests, link/catalog checks, and local data replay.
- `evidence/`: reviewed public results; `artifacts/` is ignored local working output.
- `docs/decisions/`, `docs/runbooks/`: design decisions and operation notes.

## Delivery model

Terraform establishes cloud infrastructure. GitHub Actions currently validates
code and configuration only, with no GCP identity or apply step. Later labs add
delivery through reviewed PRs and keyless identity. Kubernetes GitOps starts
when Argo CD actually pulls and reconciles desired state. A Terraform apply
workflow by itself is described here as IaC automation.

This is an intentionally small monorepo for learning. Application and platform
paths are separated; the application can move to its own repo when independent
release ownership makes that useful. [Decision](docs/decisions/0001-learning-monorepo.md).

## Evidence standard

Every completed cloud lab needs a commit, commands and tool versions, observed
outputs, a negative test, costs, and resource disposition. An authored guide,
successful static check, and successful cloud execution are different claims.
[Evidence template](evidence/TEMPLATE.md). Never publish credentials, raw
Terraform state or plans, private endpoints, or unsanitized logs.
