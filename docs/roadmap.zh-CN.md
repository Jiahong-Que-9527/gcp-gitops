> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# 由易到难：GCP 工程练习路线

从本地到基础云服务，再到数据平台、GitOps 与 AI。没有规定必须在几周内完成；
按前置条件和真实验收推进。Lab 00 的本地基线已有[验收记录](../evidence/2026-11-10-local-baseline.md)；
其他 lab 仍为计划。完成状态以 [catalog](../catalog.json) 为准。

## A 本地与基础

- [Lab 00 · 本地服务、数据契约与 Git 工作流](../labs/00-local-baseline/README.md) — 前置：无。
- [Lab 01 · 项目、IAM、结算与预算](../labs/01-sandbox-identity/README.md) — 前置：00。
- [Lab 02 · Cloud Storage 与第一个 Terraform root](../labs/02-storage-terraform/README.md) — 前置：01。
- [Lab 03 · 远程 state、锁与恢复演练](../labs/03-state-and-recovery/README.md) — 前置：02。

## B 计算与交付

- [Lab 04 · VPC、子网、路由与防火墙](../labs/04-vpc-network/README.md) — 前置：03。
- [Lab 05 · Compute Engine、磁盘与实例恢复](../labs/05-compute-vm/README.md) — 前置：04。
- [Lab 06 · 容器与 Artifact Registry](../labs/06-container-registry/README.md) — 前置：01, 00。
- [Lab 07 · Cloud Run 私有服务与版本回退](../labs/07-cloud-run/README.md) — 前置：06, 03。
- [Lab 08 · GitHub OIDC 与 Workload Identity Federation](../labs/08-keyless-ci/README.md) — 前置：07。
- [Lab 09 · CI/CD、供应链与环境晋级](../labs/09-delivery-promotion/README.md) — 前置：08。

## C 服务运维

- [Lab 10 · Logging、Monitoring、SLO 与追踪](../labs/10-observability/README.md) — 前置：07。
- [Lab 11 · Secret Manager、KMS 与凭据轮换](../labs/11-secrets-kms/README.md) — 前置：08。
- [Lab 12 · Cloud SQL、私有连接与备份恢复](../labs/12-cloud-sql/README.md) — 前置：04, 11。

## D 数据平台

- [Lab 13 · Pub/Sub、重复、重试与死信](../labs/13-pubsub-events/README.md) — 前置：07, 10。
- [Lab 14 · Eventarc、Workflows、Scheduler 与 Tasks](../labs/14-event-orchestration/README.md) — 前置：13。
- [Lab 15 · BigQuery、分区聚簇与查询成本](../labs/15-bigquery/README.md) — 前置：02, 13。
- [Lab 16 · Dataform、数据质量与血缘](../labs/16-dataform/README.md) — 前置：15。
- [Lab 17 · Beam/Dataflow、窗口与流处理](../labs/17-dataflow-beam/README.md) — 前置：13, 15。
- [Lab 18 · 批处理编排与 Composer 取舍](../labs/18-composer-batch/README.md) — 前置：16。

## E Kubernetes 与 GitOps

- [Lab 19 · GKE、集群身份与工作负载](../labs/19-gke-basics/README.md) — 前置：04, 06, 10。
- [Lab 20 · Kustomize、Helm 与配置晋级](../labs/20-kustomize-helm/README.md) — 前置：19。
- [Lab 21 · Argo CD、漂移、协调与回退](../labs/21-argocd-gitops/README.md) — 前置：20, 09。
- [Lab 22 · Gateway、DNS、TLS 与 NetworkPolicy](../labs/22-gateway-networking/README.md) — 前置：21。
- [Lab 23 · GKE Workload Identity 与策略](../labs/23-gke-identity-policy/README.md) — 前置：21, 11。

## F 可靠性与治理

- [Lab 24 · 备份、灾难恢复与故障演练](../labs/24-reliability-recovery/README.md) — 前置：12, 21。
- [Lab 25 · 负载、容量与 FinOps](../labs/25-cost-performance/README.md) — 前置：10, 15, 19。
- [Lab 28 · 目录、质量、血缘与访问治理](../labs/28-data-governance/README.md) — 前置：16。
- [Lab 29 · 审计、威胁模型与供应链检查](../labs/29-security-audit/README.md) — 前置：08, 23, 28。

## G AI 平台

- [Lab 26 · Vertex AI、模型调用与评估](../labs/26-vertex-ai/README.md) — 前置：08, 10, 15。
- [Lab 27 · 检索增强、权限与质量评估](../labs/27-rag-evaluation/README.md) — 前置：26。

## H 可展示成果

- [Lab 30 · 综合成果一：可运维的 Serverless 服务](../labs/30-capstone-serverless/README.md) — 前置：09, 10, 11, 25。
- [Lab 31 · 综合成果二：可重放的事件数据平台](../labs/31-capstone-data/README.md) — 前置：14, 16, 17, 24, 28。
- [Lab 32 · 综合成果三：GitOps 平台与受评估 AI 工作负载](../labs/32-capstone-gitops-ai/README.md) — 前置：21, 22, 23, 24, 27, 29。

## 第一条推荐路径

00 → 01 → 02 → 03 → 06 → 07 → 08 → 09 → 10。
先证明自己能把一个小服务安全交付并运维，再扩大服务覆盖。
之后偏数据岗走 13–18、28、31；偏平台岗走 04–05、19–25、29、32；AI 是 26–27。
高级实验的前置条件仍按每个 lab 检查，不跳过身份、恢复和成本。

## 覆盖范围与取舍

覆盖 IAM、计费、网络、计算、存储、数据库、容器、交付、可观测性、事件、数据仓库、
批流处理、编排、治理、安全、恢复和 AI 的常见工程能力。并不等于 GCP 所有服务。
组织级 landing zone、Shared VPC、混合云 VPN/Interconnect、大规模 Spanner/Bigtable、
GPU 训练、GKE 多集群及企业合规审计是后续按岗位需求扩展的方向；当前没有实现。

## 成果优先

以三个 capstone 的复现、故障与恢复、成本和解释能力作为求职证据。
没有实际执行的 lab 保持 planned；写好 README 不能替代使用经验。
