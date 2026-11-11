> [房玄龄·2026-11-11] 第 1 课，读取 CSV 并报告坏记录。

# 第 1 课 · 读取三行汇率，找出一条坏记录

**本课产出**是一份能指明坏记录行号的报告。你会用到 CSV 的表头、日期和十进制数。
需要 Python 3.11 或更新版本。预计 10–15 分钟。

## 1. 先读输入

打开 [rates.csv](fixtures/rates.csv)。第一行是列名，后面是三条合成观测。
每条观测有币种、日期和汇率。先用眼睛找出无法转换成数字的那条记录。

## 2. 运行脚本

```bash
python3 --version
python3 -m course.fx_csv course/fixtures/rates.csv
```

预期输出如下。

```text
accepted=2, rejected=1
line 4: fx_rate must be a decimal number
```

`line 4` 是文件里的物理行号。表头占第 1 行，所以第 3 条数据在第 4 行。
`accepted` 统计通过校验的记录，`rejected` 统计被拒绝的记录。

## 3. 读出代码的三个动作

打开 [Python 脚本](fx_csv.py)，先找 `read_rates` 里的循环。
`csv.DictReader` 用表头给每行字段命名。`parse_rate` 把日期转成 `date`，
把汇率转成 `Decimal`。校验失败时，循环记录行号和原因，然后继续读取。

## 独立练习

[练习 CSV](fixtures/rates-date-exercise.csv) 追加了一条汇率合法、日期格式不符合要求的记录。
先预测接收数、拒绝数和新增的行号，再换成这个文件运行。用自己的话解释为什么
只检查汇率会漏掉这条错误。

<details>
<summary>提示</summary>

输入格式要求 `YYYY-MM-DD`。表头也计入行号。

</details>

<details>
<summary>参考答案</summary>

```bash
python3 -m course.fx_csv course/fixtures/rates-date-exercise.csv
```

```text
accepted=2, rejected=2
line 4: fx_rate must be a decimal number
line 5: observation_date must be a valid YYYY-MM-DD date
```

</details>

[下一课 · 把校验规则写成测试](02-test-validation.md) · [课程目录](README.md)
