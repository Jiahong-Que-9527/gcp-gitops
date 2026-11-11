> [房玄龄·2026-11-11] 第 3 课，用 SQLite 查询同一结构的汇率数据。

# 第 3 课 · 用 SQL 查询、分组和去重

**本课产出**是一张去除完全重复记录的结果表。复用前两课的校验函数，
用 Python 自带的 SQLite 把合成数据装入临时内存表。预计 20 分钟。

## 1. 看原始行

打开 [SQL 练习 CSV](fixtures/rates-sql.csv)。它有四条观测，其中两条完全相同。
先运行 [SELECT 查询](sql/01-list.sql)。

```bash
python3 -m course.fx_sql course/fixtures/rates-sql.csv list
```

```csv
currency,observation_date,fx_rate
GBP,2026-10-05,0.86
USD,2026-10-05,1.10
USD,2026-10-05,1.10
USD,2026-10-06,1.11
```

`SELECT` 指定结果列，`ORDER BY` 指定显示顺序。留意 USD 的两条相同观测。

## 2. 按币种数行

运行 [GROUP BY 查询](sql/02-count-by-currency.sql)。

```bash
python3 -m course.fx_sql course/fixtures/rates-sql.csv count
```

```csv
currency,row_count
GBP,1
USD,3
```

`COUNT(*)` 统计每组的行数，其中包括重复观测。

## 3. 折叠完全相同的三列

运行 [DISTINCT 查询](sql/03-exact-duplicates.sql)。

```bash
python3 -m course.fx_sql course/fixtures/rates-sql.csv unique
```

```csv
currency,observation_date,fx_rate
GBP,2026-10-05,0.86
USD,2026-10-05,1.10
USD,2026-10-06,1.11
```

`DISTINCT` 对三列的组合去重。这里把汇率按十进制文本保存，用于练习查询形状。
同一个币种和日期出现两个不同汇率时，两行都会保留。这正是后续要用业务键
检测并处理的冲突。

## 独立练习

在练习分支打开 [SELECT 查询](sql/01-list.sql)，增加条件，只返回
`2026-10-06` 的记录。先预测有几行，再运行 `list` 检查结果。

<details>
<summary>提示</summary>

`WHERE` 写在 `FROM` 之后、`ORDER BY` 之前。

</details>

<details>
<summary>参考答案</summary>

```sql
SELECT currency, observation_date, fx_rate
FROM fx_rates
WHERE observation_date = '2026-10-06'
ORDER BY currency, observation_date;
```

结果是一行 `USD,2026-10-06,1.11`，外加表头。

</details>

[课程目录与后续安排](README.md)
