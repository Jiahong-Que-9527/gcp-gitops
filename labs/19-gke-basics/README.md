> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 19 · GKE、集群身份与工作负载

阶段：E Kubernetes 与 GitOps。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 04、lab 06、lab 10。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 比较 Autopilot 与 Standard 的责任、规格和费用。
2. 定义最小集群、独立命名空间与工作负载资源请求。
3. 用本地或隔离集群练习 Deployment、Service、probe 和 rollout。
4. 记录 API 管理访问、升级策略与集群运行费用。

## 失败与恢复练习

故意让测试 Pod readiness 失败，验证未就绪流量不会进入服务。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：集群 ADR、rollout、probe 失败与恢复。
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

- [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
