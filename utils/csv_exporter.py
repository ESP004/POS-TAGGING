import csv
from pathlib import Path


class CSVExporter:
    """
    Utility class responsible for exporting
    POS tagging results to a CSV file.
    """

    @staticmethod
    def export(file_path: str, rows: list[tuple]) -> None:

        path = Path(file_path)

        with open(
            path,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            # Header
            writer.writerow([
                "Word",
                "POS Tag",
                "Meaning"
            ])

            # Data
            writer.writerows(rows)