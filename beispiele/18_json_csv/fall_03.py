"""JSON und CSV lesen und schreiben: CSV mit Spaltennamen verarbeiten."""

import csv
from io import StringIO

buffer = StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=["name", "quantity"], delimiter=";")
writer.writeheader()
writer.writerow({"name": "Tee; grün", "quantity": 2})
buffer.seek(0)
for row in csv.DictReader(buffer, delimiter=";"):
    print(row["name"])
    print(int(row["quantity"]) + 1)
