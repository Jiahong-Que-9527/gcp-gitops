> [房玄龄·2026-11-10] Initial learning scaffold; cloud execution is pending.

# 从 WSL Ubuntu 开始

本项目的目标是获得可复现的工程经验。不要为了覆盖服务名而一次部署所有组件。
建议先完成 00 → 01 → 02 → 03，再根据路线学习；每次只推进一个实验。

## 第一次：只在本地运行

当前工作副本位于 `/home/bill/src/gcp-gitops`。
新机器先 clone；已在该目录时不要重复 clone。

```bash
cd /home/bill/src/gcp-gitops
make doctor
make check
make replay
make run
```

另开终端执行 README 的 curl。测试应覆盖合法事件、拒绝真实数据标记、重复
event_id、错误时间格式、负延迟值、无效 HTTP 请求。Ctrl-C 停止本地服务。
本地通过只证明代码与契约可运行，不证明 IAM、网络、容器或 GCP 已配置。

## 第二次：准备独立云端沙盒

安装 gcloud / Terraform / Docker / kubectl 时遵循 [官方资料](references.md)。
本轮没有安装 gcloud，也没有登录或修改任何 GCP 项目。

先在控制台选择独立练习项目和结算账户、预算提醒，再进行身份操作：

```bash
gcloud auth login
gcloud auth application-default login
gcloud auth list --filter=status:ACTIVE
gcloud projects describe YOUR_SANDBOX_PROJECT
```

CLI 登录和 Application Default Credentials 是两条认证路径。
不要把本机 ADC 文件上传到 GitHub。`.env.example` 是变量说明；需要时在本地
新建被忽略的 `.env`，确认值后 `source .env`。不得自动沿用旧项目。

```bash
gcloud projects describe "$GCP_PROJECT_ID" --format='value(projectId)'
gcloud billing projects describe "$GCP_PROJECT_ID"
```

完成 lab 01 后，再对单个 Terraform root 运行 init / validate / plan。
CI 的 validate 不需要 GCP 凭据；plan 通常需要 ADC、有效项目、API 和权限。
Terraform starter 默认使用各目录自己的本地 state；lab 03 再单独迁移远程后端。

## 每次实验的结束条件

在 evidence 模板里记录目标、实际结果、失败分析、费用、遗留资源。
删除资源前列出具体目标、数据影响和恢复方式，经明确授权再操作。
预算提醒不是停费开关，结束练习也不代表费用自动归零。

## 接下来读什么

[路线](roadmap.zh-CN.md) → [lab 00](../labs/00-local-baseline/README.md) →
[lab 01](../labs/01-sandbox-identity/README.md)。每个 guide 都说明前置条件；
进阶内容是待实现任务，不能直接当作可执行成品。
