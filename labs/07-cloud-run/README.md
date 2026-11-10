> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 07 · Cloud Run 私有服务与版本回退

阶段：B 计算与交付。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 06、lab 03。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 阅读 infra/stacks/cloud-run，用 Artifact Registry 的 digest 替换示例镜像。
2. 明确启用 API、运行身份与 invoker 权限后生成计划。
3. 部署最小副本 0、最大副本受限的认证服务。
4. 记录 revision、服务响应、日志；通过授权的新 revision 练习流量回退。

## 已提供的起点

参见 [Terraform root](../../infra/stacks/cloud-run/README.md)。

```bash
terraform -chdir=infra/stacks/cloud-run init
terraform -chdir=infra/stacks/cloud-run validate
# 按该目录 README 设置本地变量、ADC、项目、API 与权限后再运行 plan。
```

init / validate 不创建资源；plan 需要云端前置条件。本轮没有执行 apply。

## 失败与恢复练习

匿名访问应被拒绝；授权身份调用 /validate 成功；错误镜像 revision 不应替代健康流量。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：私有调用、revision 对照、回退与费用证据。
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

- [Cloud Run containers](https://docs.cloud.google.com/run/docs/deploying)
