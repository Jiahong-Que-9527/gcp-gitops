> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 30 · 综合成果一：可运维的 Serverless 服务

阶段：H 可展示成果。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 09、lab 10、lab 11、lab 25。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 以新环境从仓库复现 Cloud Run 服务，记录 setup 时间。
2. 通过 keyless pipeline 交付 digest，并验证身份与日志。
3. 执行一次坏 revision/权限故障和回退。
4. 录制 3–5 分钟英文讲解，包含费用、限制与实际结果。

## 失败与恢复练习

随机选择文档中的一次失败场景，由 runbook 独立完成诊断恢复。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：可复现 release、演示视频、架构/运维/成本说明。
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
- [Keyless deployment pipelines](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
