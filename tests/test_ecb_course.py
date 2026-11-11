"""[房玄龄·2026-11-11] Check ECB-to-course column mapping offline."""
from datetime import date
import unittest

from course.fx_ecb import normalize_rates

HEADER = "KEY,FREQ,CURRENCY,CURRENCY_DENOM,EXR_TYPE,EXR_SUFFIX,TIME_PERIOD,OBS_VALUE\n"


class EcbCsvTests(unittest.TestCase):
    start = date(2024, 1, 5)
    end = date(2024, 1, 9)

    def test_maps_ecb_columns_and_orders_observations(self):
        # Synthetic values in the shape of ECB's CSV response.
        raw = HEADER + (
            "EXR.D.USD.EUR.SP00.A,D,USD,EUR,SP00,A,2024-01-09,1.22\n"
            "EXR.D.USD.EUR.SP00.A,D,USD,EUR,SP00,A,2024-01-05,1.10\n"
        )
        self.assertEqual(normalize_rates(raw, self.start, self.end), [
            ("USD", "2024-01-05", "1.10"),
            ("USD", "2024-01-09", "1.22"),
        ])

    def test_rejects_wrong_series_and_missing_observations(self):
        with self.assertRaisesRegex(ValueError, "unexpected exchange-rate series"):
            normalize_rates(HEADER + "EXR.D.GBP.EUR.SP00.A,D,GBP,EUR,SP00,A,2024-01-05,0.9\n", self.start, self.end)
        with self.assertRaisesRegex(ValueError, "no observations"):
            normalize_rates(HEADER, self.start, self.end)
