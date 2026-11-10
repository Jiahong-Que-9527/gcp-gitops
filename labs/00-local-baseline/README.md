> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 00 · 本地服务、数据契约与 Git 工作流

阶段：A 本地与基础。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

无；Python 3.11+。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 运行 make check、make replay，理解 synthetic=true 的约束。
2. 启动 make run，以 curl 检查 /healthz、/version 和 /validate。
3. 建立一个小分支，修改 APP_VERSION 后观察版本响应；提交 PR，不覆盖他人修改。

## 可以直接执行

```bash
make doctor
make check
make replay
make run
```

另一个终端：

```bash
curl --fail http://127.0.0.1:8080/healthz
curl --fail -H 'Content-Type: application/json' --data-binary @samples/events.json http://127.0.0.1:8080/validate
```

成功响应应显示 accepted=3、mean_delay_minutes=5.0；数据仅为合成样例。

## 失败与恢复练习

提交重复 event_id、无时区时间和非 synthetic 事件，确认得到明确拒绝并保留输出。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：测试结果、一次小 PR 和本地 HTTP 验证记录。
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
