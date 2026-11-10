> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 29 · 审计、威胁模型与供应链检查

阶段：F 可靠性与治理。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 08、lab 23、lab 28。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 列出 GitHub、CI、云 IAM、数据与模型边界的威胁。
2. 区分 Admin Activity 与 Data Access 日志，评估启用/保留费用。
3. 检查过宽角色、public access、密钥、镜像和依赖风险。
4. 形成按证据优先级排序的修复 PR，不发布未脱敏日志。

## 失败与恢复练习

在隔离资源执行可识别的拒绝操作，验证审计可追溯主体与调用链。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：威胁模型、审计样例、修复前后证据。
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

- [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)
