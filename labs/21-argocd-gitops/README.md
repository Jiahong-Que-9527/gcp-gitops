> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 21 · Argo CD、漂移、协调与回退

阶段：E Kubernetes 与 GitOps。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 20、lab 09。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 先在独立环境安装固定版本 Argo CD，配置受限 AppProject。
2. 阅读 gitops/argocd/event-api.yaml，首次使用人工 sync，不开启 prune。
3. 用 PR 更改已发布镜像 digest，观察 Git revision 和实际 rollout。
4. 演练 drift；理解 selfHeal、prune 和 revert 的不同授权/数据影响。

## 失败与恢复练习

有界修改测试 Deployment 副本数，记录 OutOfSync；授权启用 selfHeal 后验证恢复。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：sync 记录、漂移实验、Git revert 与恢复。
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
