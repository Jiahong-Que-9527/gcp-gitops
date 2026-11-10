> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 28 · 目录、质量、血缘与访问治理

阶段：F 可靠性与治理。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 16。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 整理资产所有者、schema、质量和保留规则。
2. 用 Dataplex 当前产品能力登记实验数据资产，核对服务名称变化。
3. 为合成敏感列练习列级/行级访问规则和脱敏。
4. 关联 ingestion、transform、mart 和消费端的血缘。

## 失败与恢复练习

无权主体无法读取限制列/行，授权主体得到预期数据，并解释导出边界。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：目录记录、权限测试、血缘与保留说明。
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

- [Dataplex data governance](https://docs.cloud.google.com/dataplex/docs/introduction)
