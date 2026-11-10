> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 04 · VPC、子网、路由与防火墙

阶段：B 计算与交付。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 03。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 使用 infra/stacks/network 建立自定义 VPC 与一个私有 Google 访问子网。
2. 画出子网、隐含规则、路由和区域边界。
3. 设计仅允许必要身份/网段的访问；默认不建公网入站规则。
4. 比较 Private Google Access、Cloud NAT、Private Service Connect 的用途和费用。

## 已提供的起点

参见 [Terraform root](../../infra/stacks/network/README.md)。

```bash
terraform -chdir=infra/stacks/network init
terraform -chdir=infra/stacks/network validate
# 按该目录 README 设置本地变量、ADC、项目、API 与权限后再运行 plan。
```

init / validate 不创建资源；plan 需要云端前置条件。本轮没有执行 apply。

## 失败与恢复练习

用后续测试 VM 验证无允许规则时连接被拒绝，结合流日志或连通性诊断解释原因。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：网络 ADR、路由/规则清单、连通性正反测试。
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

- [VPC overview](https://docs.cloud.google.com/vpc/docs/overview)
