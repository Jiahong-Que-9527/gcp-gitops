> [房玄龄·2026-11-11] 第 2 课，用测试表达数据校验规则。

# 第 2 课 · 把校验规则写成测试

**本课产出**是一条你能独立写出的数据校验测试。复用上一课的 Python 函数和 CSV。
预计 15–20 分钟。

## 1. 运行 Python 校验测试

```bash
python3 -m unittest discover -s tests -p test_fx_course.py -k FxValidationTests -v
```

预期显示 `Ran 4 tests` 和 `OK`。测试覆盖正确汇率、错误日期、非有限值或非正数，
以及读取一份含坏记录的 CSV。一个测试里的多个输入由 `subTest` 分别报告。

## 2. 对照函数和测试

打开 [测试文件](../tests/test_fx_course.py) 和 [校验函数](fx_csv.py)。
先看 `test_valid_rate_preserves_decimal`，找出输入和期望值。
再看 `test_invalid_date_is_rejected_even_with_valid_rate`。
这个测试只改日期，能让你分辨失败来自哪一条规则。

## 独立练习

在你自己的练习分支上，给 `FxValidationTests` 加一条测试。
保留合法日期和汇率，只把币种换成 `usd`。预测它会通过校验还是抛出异常，
再运行刚才的命令。写完后，试着把预期故意写错一次，找到失败报告里的方法名和原因，
然后改回正确预期。

<details>
<summary>提示</summary>

`dict(self.row, currency="usd")` 会复制原有输入，只改币种。
用 `assertRaisesRegex` 检查异常类型和报错字段。

</details>

<details>
<summary>参考答案</summary>

```python
def test_lowercase_currency_is_rejected(self):
    with self.assertRaisesRegex(ValueError, "currency"):
        parse_rate(dict(self.row, currency="usd"))
```

加入方法后，前面的命令应显示 `Ran 5 tests` 和 `OK`。

</details>

[下一课 · 用 SQL 查询、分组和去重](03-query-sql.md) · [课程目录](README.md)
