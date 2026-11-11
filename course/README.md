> [房玄龄·2026-11-11] 新增汇率数据管道实战课程入口。

# 从 CSV 到 GCP 的汇率数据管道

从一份合成汇率 CSV 出发，逐步学会用 Python 校验数据、用 SQL 建模，
再把同一类工作负载部署到 GCP。前 3 课只需要 Python 3.11 或更新版本。
如果已经在 WSL 克隆仓库，先进入仓库根目录。第一次下载时可以执行：

```bash
git clone https://github.com/Jiahong-Que-9527/gcp-gitops.git
cd gcp-gitops
```

每课的命令都从仓库根目录执行。打算修改测试或 SQL 时，可以先执行
`git switch -c practice/fx-basics`，把你的练习留在自己的分支。

## 可以直接做的课

1. [读取三行汇率，找出一条坏记录](01-read-csv.md)。
   学会 CSV 表头、字段转换、行号和错误报告。
2. [把校验规则写成测试](02-test-validation.md)。
   用正例、反例和同一份 CSV 检查规则。
3. [用 SQL 查询、分组和去重](03-query-sql.md)。
   在 Python 自带的 SQLite 中观察重复行对查询的影响。

先运行给定命令，对照预期输出。做独立练习时先写下你的预测，
再打开提示或参考答案。每课的结果都可以在终端直接核对。

## 后续课程安排

4. **Python 数据提取与增量 SQL**。用固定日期区间调用 ECB 的公开接口，
   学习超时、重试、快照、业务键冲突和有界回填。
5. **第一次使用 GCP**。选择沙盒，核对项目、区域、身份和预算，
   然后从 Cloud Storage 加载数据到 BigQuery。
   [现有沙盒指南](../labs/01-sandbox-identity/README.md) ·
   [现有 BigQuery 指南](../labs/15-bigquery/README.md)
6. **Cloud Run Job 与恢复**。从手动运行开始，跟踪执行和日志，
   练习缺数阻止发布，以及补齐后按原区间重跑。
7. **Terraform、GitHub Actions 与 Airflow**。复现已经理解的资源，
   再学习自动验证、按数据区间调度和回填。
8. **Pub/Sub、Beam 与 Dataflow**。验证重复、乱序、迟到和对账，
   先做本地实验，再做云端扩展。

第 4 课起是后续开发计划。更广的 GCP、Kubernetes 和 AI 实验见
[现有实验索引](../docs/roadmap.zh-CN.md)。
