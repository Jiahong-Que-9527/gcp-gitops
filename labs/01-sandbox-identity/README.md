> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 01 · 项目、IAM、结算与预算

阶段：A 本地与基础。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 00。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 建立独立 sandbox，记录项目、区域、结算账户和负责人。
2. 区分个人身份、ADC、服务账号及资源级权限；只读检查当前身份。
3. 设置预算提醒，列出未来各服务可能持续计费的资源。
4. 定义应用运行身份和部署身份的职责，禁止把 Owner 当作通用运行角色。

## 操作清单：选项目、核验身份、设置预算

预计 30–60 分钟。先安装 [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk)，
在控制台建立或选择一个**专用实验项目**。如果没有合适的结算账号或创建权限，
记录阻塞并停在本地；不要借用公司或现有生产项目。项目 ID 与显示名称不同。

在仓库根目录创建本地 `.env`（Git 已忽略），按 `.env.example` 填写专用项目和区域。
不要把真实身份、账单账号、导出的凭据放进该文件的示例版本或 evidence。

```bash
source .env
gcloud auth login
gcloud auth list --filter=status:ACTIVE --format='value(account)'
gcloud projects describe "$GCP_PROJECT_ID" --format='value(projectId,lifecycleState)'
gcloud billing projects describe "$GCP_PROJECT_ID" --format='value(billingEnabled)'
gcloud services list --enabled --project="$GCP_PROJECT_ID" --format='value(config.name)'
```

确认返回的是专用项目、状态 ACTIVE、结算状态符合预期。将项目作为 Cloud Billing
预算过滤条件，填写自己的金额和接收人，设实际/预测阈值。确认提醒的接收与配置，
无需为了触发提醒制造费用。预算提醒不是硬上限。

为 lab 02 的 Terraform 建立本机 ADC，和 CLI 登录分开：

```bash
gcloud auth application-default login
```

身份小表建议按「操作者 / 部署身份 / 运行身份 / 资源 / 所需操作」记录。此阶段
不生成服务账号密钥，也不需要给 CI 云权限。原始账号和项目标识只留在本机。

## 失败与恢复练习

使用无权限测试身份读取一个私有资源，保存拒绝信息；不要撤销自己的唯一管理入口。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：身份权限矩阵、预算设置证据、资源命名规则。
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

- [Google Cloud setup](https://docs.cloud.google.com/docs/enterprise/setup-checklist)
- [Budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)
