> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 32 · 综合成果三：GitOps 平台与受评估 AI 工作负载

阶段：H 可展示成果。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 21、lab 22、lab 23、lab 24、lab 27、lab 29。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 从明确的集群基线通过 Git 重建无状态工作负载。
2. 演示 digest 晋级、漂移检测、回退和工作负载身份。
3. 在平台上增加已评估 AI 功能，单独声明模型与平台结果。
4. 以面试题形式解释 GKE/Cloud Run、成本、恢复和信任边界。

## 失败与恢复练习

测试 Git 配置偏差、无权模型调用和一项回答质量失败，分别验证恢复/拒绝/降级。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：平台演示、AI 评估、设计 ADR、故障与成本证据。
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

- [Argo CD getting started](https://argo-cd.readthedocs.io/en/stable/getting_started/)
- [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)
