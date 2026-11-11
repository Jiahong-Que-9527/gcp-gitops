"""[房玄龄·2026-11-11] Read and validate synthetic FX rates for lessons 1 and 2."""
import argparse
import csv
from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

COLUMNS = ("currency", "observation_date", "fx_rate")


@dataclass(frozen=True)
class FxRate:
    currency: str
    observation_date: date
    fx_rate: Decimal


def parse_rate(row: dict[str, str]) -> FxRate:
    currency = row["currency"].strip()
    if not (len(currency) == 3 and currency.isascii() and currency.isalpha() and currency.isupper()):
        raise ValueError("currency must be three uppercase ASCII letters")

    date_text = row["observation_date"].strip()
    try:
        observation_date = date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("observation_date must be a valid YYYY-MM-DD date") from None
    if observation_date.isoformat() != date_text:
        raise ValueError("observation_date must be a valid YYYY-MM-DD date")

    try:
        fx_rate = Decimal(row["fx_rate"].strip())
    except InvalidOperation:
        raise ValueError("fx_rate must be a decimal number") from None
    if not fx_rate.is_finite() or fx_rate <= 0:
        raise ValueError("fx_rate must be finite and positive")

    return FxRate(currency, observation_date, fx_rate)


def read_rates(path: Path) -> tuple[list[FxRate], list[tuple[int, str]]]:
    accepted = []
    rejected = []
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, strict=True)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise ValueError("expected header: " + ",".join(COLUMNS))
        for row in reader:
            try:
                if None in row or None in row.values():
                    raise ValueError("expected exactly three fields")
                accepted.append(parse_rate(row))
            except ValueError as error:
                rejected.append((reader.line_num, str(error)))
    return accepted, rejected


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a synthetic FX CSV file.")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    try:
        accepted, rejected = read_rates(args.csv_path)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"could not read FX CSV: {error}\n")
    print(f"accepted={len(accepted)}, rejected={len(rejected)}")
    for line, reason in rejected:
        print(f"line {line}: {reason}")


if __name__ == "__main__":
    main()
