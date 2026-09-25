"""Datum, Zeit und Zufallswerte: Datum lesen und Tage addieren."""

from datetime import date, timedelta

start = date.fromisoformat("2026-09-25")
end = start + timedelta(days=7)
print(end.isoformat())
print((end - start).days)
print(end.strftime("%d.%m.%Y"))
