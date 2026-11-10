> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 02 · Cloud Storage 与第一个 Terraform root

阶段：A 本地与基础。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 01。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 阅读 infra/stacks/storage，检查 bucket 名称唯一性和区域。
2. 完成 init、validate、plan，审阅变更后再请求具体 apply 授权。
3. 用仅含 synthetic 的样例验证对象读写、版本和权限。
4. 记录 force_destroy=false 与 public_access_prevention 的作用。

## 已提供的起点

参见 [Terraform root](../../infra/stacks/storage/README.md)。

```bash
terraform -chdir=infra/stacks/storage init
terraform -chdir=infra/stacks/storage validate
# 按该目录 README 设置本地变量、ADC、项目、API 与权限后再运行 plan。
```

init / validate 不创建资源；plan 需要云端前置条件。本轮没有执行 apply。

## 操作清单：第一个可审阅的云变更

先完成 lab 01，确认 sandbox、预算、ADC 和 Storage API。下列命令从仓库根目录执行；
Terraform 可使用系统安装，或给当前 shell 加上本地校验工具路径：

```bash
export PATH="$PWD/.tools:$PATH"
source .env
gcloud projects describe "$GCP_PROJECT_ID" --format='value(projectId)'
gcloud services list --enabled --project="$GCP_PROJECT_ID" \
  --filter='config.name=storage.googleapis.com' --format='value(config.name)'
```

如果缺 API，先明确具体项目和变更范围再启用。创建新的忽略文件
`infra/stacks/storage/local.tfvars`，以示例为参考，填写 `project_id`、`region` 和
`environment`。确保名字与现有 bucket 不冲突；不要复用已有 state 或 bucket。

```bash
terraform -chdir=infra/stacks/storage init -input=false -lockfile=readonly
terraform -chdir=infra/stacks/storage validate
terraform -chdir=infra/stacks/storage plan -var-file=local.tfvars -out=storage.tfplan
terraform -chdir=infra/stacks/storage show -no-color storage.tfplan
```

预期是新增一个私有版本化 bucket，零修改、零删除。检查目标项目、区域、标签、
public access prevention 和 force_destroy 后，再授权 apply 当前保存的 plan。
plan 和 state 均保留在忽略文件中，不上传完整输出。apply 属于实际创建资源，
在本次初始化中没有执行。

如果已完成授权 apply，使用 Terraform 输出而不是手填生产 bucket 名：

```bash
BUCKET="$(terraform -chdir=infra/stacks/storage output -raw bucket_name)"
gcloud storage buckets describe "gs://$BUCKET"
gcloud storage cp --no-clobber samples/events.ndjson "gs://$BUCKET/labs/02/events.ndjson"
gcloud storage objects describe "gs://$BUCKET/labs/02/events.ndjson"
gcloud storage cat "gs://$BUCKET/labs/02/events.ndjson"
```

校验对象代次与 3 条合成记录，确认没有公开授权。再次尝试对象写入前选择新的
测试对象，只有版本实验才有意生成同名新版本。记录对象、版本保留、计费和去向。

## 失败与恢复练习

使用未授权身份读取对象应失败；上传新对象版本后验证旧版本仍可定位，不删除原件。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：Terraform plan 摘要、权限正反测试、对象版本证据。
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

- [Cloud Storage with Terraform](https://docs.cloud.google.com/storage/docs/terraform-for-cloud-storage)
