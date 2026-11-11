"""[房玄龄·2026-11-11] Run lesson 3 queries against an in-memory SQLite table."""
import argparse
from contextlib import closing
import csv
from pathlib import Path
import sqlite3
import sys

from course.fx_csv import read_rates

SQL_DIR = Path(__file__).with_name("sql")
QUERIES = {
    "list": "01-list.sql",
    "count": "02-count-by-currency.sql",
    "unique": "03-exact-duplicates.sql",
}


def query_rates(csv_path: Path, query_path: Path):
    rates, rejected = read_rates(csv_path)
    if rejected:
        line, reason = rejected[0]
        raise ValueError(f"line {line}: {reason}; inspect the CSV before running SQL")
    with closing(sqlite3.connect(":memory:")) as connection:
        # Store the decimal representation as text in this local exercise.
        connection.execute("""
            CREATE TABLE fx_rates (
                currency TEXT NOT NULL,
                observation_date TEXT NOT NULL,
                fx_rate TEXT NOT NULL
            )
        """)
        connection.executemany(
            "INSERT INTO fx_rates VALUES (?, ?, ?)",
            [(rate.currency, rate.observation_date.isoformat(), str(rate.fx_rate)) for rate in rates],
        )
        cursor = connection.execute(query_path.read_text(encoding="utf-8"))
        return [column[0] for column in cursor.description], cursor.fetchall()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a lesson 3 SQLite query.")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("query", choices=QUERIES)
    args = parser.parse_args()
    try:
        columns, rows = query_rates(args.csv_path, SQL_DIR / QUERIES[args.query])
    except (OSError, ValueError, csv.Error, sqlite3.Error) as error:
        parser.exit(1, f"could not run SQL exercise: {error}\n")
    output = csv.writer(sys.stdout, lineterminator="\n")
    output.writerow(columns)
    output.writerows(rows)


if __name__ == "__main__":
    main()
