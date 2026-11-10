> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 26 · Vertex AI、模型调用与评估

阶段：G AI 平台。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 08、lab 10、lab 15。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 使用合成文本和固定评估集，区分托管模型调用与自建 endpoint。
2. 实现模型版本、提示词版本、超时、重试和响应记录。
3. 测量准确性/任务得分、p95 延迟、token 和费用。
4. 训练/微调只作为后续独立实验，不伪造效果。

## 失败与恢复练习

模拟 429、无效输入和超时，验证有界重试与明确降级。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：评估集、脚本、可复现结果与模型选择 ADR。
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

- [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)
