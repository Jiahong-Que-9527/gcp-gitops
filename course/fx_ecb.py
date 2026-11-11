"""[房玄龄·2026-11-11] Fetch a fixed window of USD reference rates for lesson 4.1."""
import argparse
import csv
from datetime import date
from io import StringIO
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from course.fx_csv import COLUMNS

SERIES = "EXR.D.USD.EUR.SP00.A"
ENDPOINT = "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A"
ECB_COLUMNS = ("KEY", "CURRENCY", "CURRENCY_DENOM", "TIME_PERIOD", "OBS_VALUE")


def normalize_rates(raw_csv: str, start: date, end: date) -> list[tuple[str, str, str]]:
    reader = csv.DictReader(StringIO(raw_csv, newline=""), strict=True)
    if not set(ECB_COLUMNS).issubset(reader.fieldnames or ()):
        raise ValueError("ECB response is missing expected CSV columns")

    rows = []
    for row in reader:
        if not all(row.get(column) for column in ECB_COLUMNS):
            raise ValueError(f"ECB line {reader.line_num}: missing required field")
        if (row["KEY"], row["CURRENCY"], row["CURRENCY_DENOM"]) != (SERIES, "USD", "EUR"):
            raise ValueError(f"ECB line {reader.line_num}: unexpected exchange-rate series")
        observation_date = date.fromisoformat(row["TIME_PERIOD"])
        if not start <= observation_date <= end:
            raise ValueError(f"ECB line {reader.line_num}: observation is outside the requested dates")
        rows.append((row["CURRENCY"], observation_date.isoformat(), row["OBS_VALUE"]))
    if not rows:
        raise ValueError("ECB returned no observations for the requested dates")
    return sorted(rows, key=lambda row: row[1])


def main() -> None:
    parser = argparse.ArgumentParser(description="Download ECB USD-per-EUR rates as a course CSV.")
    parser.add_argument("--start", required=True, type=date.fromisoformat, metavar="YYYY-MM-DD")
    parser.add_argument("--end", required=True, type=date.fromisoformat, metavar="YYYY-MM-DD")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.start > args.end:
        parser.error("--start must be on or before --end")
    if args.output.exists():
        parser.error("output already exists; choose a new filename")
    if not args.output.parent.is_dir():
        parser.error("output directory does not exist; create it first")

    query = urlencode({
        "startPeriod": args.start.isoformat(),
        "endPeriod": args.end.isoformat(),
        "format": "csvdata",
        "detail": "dataonly",
    })
    url = f"{ENDPOINT}?{query}"
    print(f"source={url}", flush=True)
    request = Request(url, headers={"User-Agent": "gcp-gitops-fx-course/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            raw_csv = response.read().decode("utf-8-sig")
        rows = normalize_rates(raw_csv, args.start, args.end)
        with args.output.open("x", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(COLUMNS)
            writer.writerows(rows)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"could not fetch ECB rates: {error}\n")

    print(f"saved={len(rows)}, path={args.output}")


if __name__ == "__main__":
    main()
