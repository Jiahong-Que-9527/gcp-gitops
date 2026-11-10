> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 13 · Pub/Sub、重复、重试与死信

阶段：D 数据平台。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 07、lab 10。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 使用 event_id 发布同一套样例数据，设计消费者幂等策略。
2. 明确 ack deadline、重试、保留期限和死信转发 IAM。
3. 记录发送、成功、重复、失败和死信计数。
4. 验证精确一次交付的适用边界，不能替代跨存储业务幂等。

## 失败与恢复练习

重复发送、注入坏事件、故意延迟 ack，观察重投与有界重放。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：事件契约、去重测试、计数对账与死信恢复。
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

- [Pub/Sub exactly-once boundaries](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)
