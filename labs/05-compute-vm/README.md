> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 05 · Compute Engine、磁盘与实例恢复

阶段：B 计算与交付。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 04。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 创建一台短时小型 VM，选择 OS Login/IAP 或既有受控管理路径。
2. 区分启动盘、数据盘、快照和独立备份。
3. 通过启动脚本运行样例服务，观察重启后的状态。
4. 记录停止实例后仍保留并计费的磁盘、地址和备份。

## 失败与恢复练习

重启测试进程并验证恢复；从授权的磁盘副本在隔离实例读取测试文件。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：实例配置、访问解释、恢复计时和费用清单。
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

- [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
