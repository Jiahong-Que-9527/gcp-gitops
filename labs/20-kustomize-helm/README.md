> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 20 · Kustomize、Helm 与配置晋级

阶段：E Kubernetes 与 GitOps。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 19。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 渲染 gitops/workloads/event-api/overlays/dev 并审阅资源。
2. 为 stage 设计不同副本/配置，保持镜像 digest 一致。
3. 对比 Helm chart 复用与 Kustomize patch，避免同时管理同一对象。
4. 添加 schema/render 检查；占位镜像替换前不可部署。

## 失败与恢复练习

构造无效 patch 或缺失配置，验证渲染检查提前失败。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：渲染 diff、版本晋级 PR、选择 ADR。
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

- [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
