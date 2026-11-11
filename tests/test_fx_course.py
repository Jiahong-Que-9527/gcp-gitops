"""[房玄龄·2026-11-11] Regression examples used in the local FX course."""
from datetime import date
from decimal import Decimal
from pathlib import Path
import unittest

from course.fx_csv import FxRate, parse_rate, read_rates
from course.fx_sql import SQL_DIR, query_rates

FIXTURES = Path(__file__).resolve().parents[1] / "course" / "fixtures"


class FxValidationTests(unittest.TestCase):
    def setUp(self):
        self.row = {"currency": "USD", "observation_date": "2026-10-05", "fx_rate": "1.10"}

    def test_valid_rate_preserves_decimal(self):
        self.assertEqual(parse_rate(self.row), FxRate("USD", date(2026, 10, 5), Decimal("1.10")))

    def test_invalid_date_is_rejected_even_with_valid_rate(self):
        for value in ("05/10/2026", "20261005", "2026-02-30"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "observation_date"):
                    parse_rate(dict(self.row, observation_date=value))

    def test_nonfinite_and_nonpositive_rates_are_rejected(self):
        for value in ("NaN", "Infinity", "0", "-1.10"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "finite and positive"):
                    parse_rate(dict(self.row, fx_rate=value))

    def test_read_fixture_with_a_bad_date(self):
        rates, rejected = read_rates(FIXTURES / "rates-date-exercise.csv")
        self.assertEqual(len(rates), 2)
        self.assertEqual([line for line, _ in rejected], [4, 5])
        self.assertIn("observation_date", rejected[1][1])


class FxSqlTests(unittest.TestCase):
    def test_grouped_counts_include_the_duplicate(self):
        columns, rows = query_rates(FIXTURES / "rates-sql.csv", SQL_DIR / "02-count-by-currency.sql")
        self.assertEqual(columns, ["currency", "row_count"])
        self.assertEqual(rows, [("GBP", 1), ("USD", 3)])

    def test_distinct_preserves_the_next_observation_date(self):
        _, rows = query_rates(FIXTURES / "rates-sql.csv", SQL_DIR / "03-exact-duplicates.sql")
        self.assertEqual(rows, [
            ("GBP", "2026-10-05", "0.86"),
            ("USD", "2026-10-05", "1.10"),
            ("USD", "2026-10-06", "1.11"),
        ])
