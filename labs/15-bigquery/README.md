> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 15 · BigQuery、分区聚簇与查询成本

阶段：D 数据平台。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 02、lab 13。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 使用 infra/stacks/analytics 建立小型 dataset 和分区表。
2. 加载 samples/events.ndjson，核对 schema 与行数。
3. 运行 samples/daily_delays.sql，比较干跑扫描量与受限查询。
4. 验证分区过滤、maximum_bytes_billed 与数据过期的区别。

## 已提供的起点

参见 [Terraform root](../../infra/stacks/analytics/README.md)。

```bash
terraform -chdir=infra/stacks/analytics init
terraform -chdir=infra/stacks/analytics validate
# 按该目录 README 设置本地变量、ADC、项目、API 与权限后再运行 plan。
```

init / validate 不创建资源；plan 需要云端前置条件。本轮没有执行 apply。

## 查询与加载示例（需要先授权创建云资源）

```bash
bq --location="$GCP_REGION" load --source_format=NEWLINE_DELIMITED_JSON "$GCP_PROJECT_ID:gcp_gitops_dev.events" samples/events.ndjson
# 编辑一份本地 SQL，将 YOUR_PROJECT 替换为实际 sandbox 项目后：
bq query --use_legacy_sql=false --dry_run < artifacts/daily_delays.local.sql
bq query --use_legacy_sql=false --maximum_bytes_billed=10000000 < artifacts/daily_delays.local.sql
```

输出前检查项目和区域。该查询是演示聚合；需要在后续 lab 实现幂等写入。

## 失败与恢复练习

查询缺少分区过滤应失败；重复加载同 event_id 后用明确 MERGE/去重策略对账。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：表设计、SQL、扫描量比较、去重证据。
- 使用 [evidence 模板](../../evidence/TEMPLATE.md)，链接 commit / CI run；
  静态检查、本地模拟和 GCP 实测须分开标注。

## 成本与收尾

执行前查阅服务定价；记录本次时长/请求量/扫描量和剩余资源。
本地实验不调用云 API；云实验结束后仍可能有存储、日志、集群或网络费用。
按 [资源生命周期规则](../../docs/cost-and-lifecycle.md) 逐项审阅，不自动 destroy。

## 面试复述

解释为什么选这个服务、权限如何收敛、发生了什么失败、如何恢复、成本如何衡量。
只描述实际完成并有证据的部分，写出仍未验证的限制。

## 官方资料

- [BigQuery cost control](https://docs.cloud.google.com/bigquery/docs/best-practices-costs)
