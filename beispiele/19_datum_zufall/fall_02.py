"""Datum, Zeit und Zufallswerte: Zeitzonen ausdrücklich angeben."""

from datetime import datetime, timezone, timedelta

moment = datetime(2026, 9, 25, 12, 0, tzinfo=timezone.utc)
print(moment.isoformat())
fixed_offset = timezone(timedelta(hours=2))
print(moment.astimezone(fixed_offset).isoformat())
