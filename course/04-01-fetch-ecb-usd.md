> [房玄龄·2026-11-11] 第 4.1 课，从 ECB API 提取固定区间的 USD 汇率。

# 第 4.1 课 · 从 ECB API 下载几天 USD 汇率

**本课产出**是一份本地 CSV，以及你能用 Python 和 SQL 核对的观测日期和行数。
需要 Python 3.11 或更新版本及网络。命令在仓库根目录运行，预计 15–20 分钟。

## 1. 先读懂请求

本课选 ECB 的日频序列 `EXR.D.USD.EUR.SP00.A`。`USD` 是报价币种，
`EUR` 是基准币种。`1.0921` 表示 1 欧元对应 1.0921 美元。
起止日期都包含在请求范围里。2024 年 1 月 5 日到 9 日包含一个周末。
先预测会返回几条观测，再运行。[ECB 数据 API](https://data.ecb.europa.eu/help/api/data)
· [USD 日频序列](https://data.ecb.europa.eu/data/datasets/EXR/EXR.D.USD.EUR.SP00.A)

## 2. 下载并保存为课程 CSV

```bash
mkdir -p artifacts
python3 -m course.fx_ecb --start 2024-01-05 --end 2024-01-09 \
  --output artifacts/ecb-usd-2024-01-05-to-09.csv
```

脚本先打印完整的来源 URL。下载成功后应显示：

```text
saved=3, path=artifacts/ecb-usd-2024-01-05-to-09.csv
```

打开 [提取脚本](fx_ecb.py)，找出 `startPeriod`、`endPeriod` 和 `format=csvdata`。
`normalize_rates` 把 API 的 `CURRENCY`、`TIME_PERIOD` 和 `OBS_VALUE`
映射成前几课用过的 `currency`、`observation_date` 和 `fx_rate`。
可以在浏览器打开终端打印的 URL，亲自对照原始表头。
`artifacts/` 已被 Git 忽略。重做时换一个输出文件名，保留第一次的结果。

## 3. 用前两课的 Python 校验

```bash
python3 -m course.fx_csv artifacts/ecb-usd-2024-01-05-to-09.csv
python3 -m unittest discover -s tests -p test_fx_course.py -k FxValidationTests -v
```

校验输出应为 `accepted=3, rejected=0`。离线测试应显示 `Ran 4 tests` 和
`OK`。CSV 校验检查每一行的字段，SQL 查询会复用同一个校验函数。
测试用合成输入验证代码规则，这次下载的文件由第一条命令单独校验。

## 4. 用第 3 课的 SQL 核对日期和行数

```bash
python3 -m course.fx_sql artifacts/ecb-usd-2024-01-05-to-09.csv list
python3 -m course.fx_sql artifacts/ecb-usd-2024-01-05-to-09.csv count
```

`list` 预期输出：

```csv
currency,observation_date,fx_rate
USD,2024-01-05,1.0921
USD,2024-01-08,1.0946
USD,2024-01-09,1.094
```

`count` 预期输出：

```csv
currency,row_count
USD,3
```

对照日期，1 月 6 日和 7 日是周末。示例数值来自对 ECB 的实测请求，
源站修订后以实际响应为准。

## 独立练习

把起始日改成 1 月 8 日，结束日保持 1 月 9 日。用一个新文件名保存。
先预测 CSV 校验会接受几条、SQL 会列出哪些日期，再运行验证。

<details>
<summary>提示</summary>

只改 `--start` 和 `--output`。沿用 `list` 和 `count`，
把它们的输入路径换成这次保存的 CSV。

</details>

<details>
<summary>参考答案</summary>

```bash
python3 -m course.fx_ecb --start 2024-01-08 --end 2024-01-09 \
  --output artifacts/ecb-usd-2024-01-08-to-09.csv
python3 -m course.fx_csv artifacts/ecb-usd-2024-01-08-to-09.csv
python3 -m course.fx_sql artifacts/ecb-usd-2024-01-08-to-09.csv list
python3 -m course.fx_sql artifacts/ecb-usd-2024-01-08-to-09.csv count
```

应保存 2 条，校验输出 `accepted=2, rejected=0`。SQL 明细如下，
分组计数为 `USD,2`。

```csv
currency,observation_date,fx_rate
USD,2024-01-08,1.0946
USD,2024-01-09,1.094
```

</details>

如果请求超时，等片刻后再运行。请求或响应解析失败时，脚本会报告错误。
记录来源 URL、保存路径和 SQL 行数，就完成了本课。

[上一课 · 用 SQL 查询、分组和去重](03-query-sql.md) · [课程目录](README.md)
