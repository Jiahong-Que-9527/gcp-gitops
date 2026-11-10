> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# Lab 08 · GitHub OIDC 与 Workload Identity Federation

阶段：B 计算与交付。状态以 [catalog](../../catalog.json) 和 evidence 为准。

## 前置条件

lab 07。
云端任务需要独立 sandbox、已核验身份、相关 API/权限和预算。本文的云操作
是后续实验说明；只有 lab 00 和提供的 starter 可以从当前仓库直接开始验证。

## 实验任务

1. 建立独立部署服务账号与受限 workload identity pool/provider。
2. 用不可变 repository/owner ID 限制信任，再限制 main 分支或受保护 environment。
3. 只授予部署所需角色与特定运行身份上的 actAs。
4. 新增手动认证 smoke workflow；只在受信分支获取 id-token。

## 信任边界

GitHub 账号的公开 owner ID 为 `252800845`；repository ID 在创建后从 API 读取。
实际配置时用当前 `gh api repos/Jiahong-Que-9527/gcp-gitops --jq .id` 核验。
Provider 映射 `google.subject=assertion.sub`，并映射 owner/repository ID；
CEL 条件同时限制 owner ID、repository ID 和允许 ref/environment。
限制 service account impersonation 的 principalSet，并将 actAs 限定到具体运行身份。
`id-token: write` 只放在需要的受信 job；fork PR 的验证 job 不接触云身份。
本仓库初始 CI 没有 OIDC 权限，也没有隐藏的云部署 workflow。

## 失败与恢复练习

验证不匹配的仓库、分支或 audience 无法换取凭据；不要在公共 PR 日志输出 token。
限定在专用测试资源上，保留原始数据和管理入口；破坏性操作另列具体目标申请授权。

## 验收与成果

- 正向测试必须实际通过，保留命令、时间、版本与观察结果。
- 完成上面的负向测试，解释预期和实际结果，再验证恢复。
- 交付：脱敏信任条件、成功认证 run、拒绝测试。
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

- [Keyless deployment pipelines](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
