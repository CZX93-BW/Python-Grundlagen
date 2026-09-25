"""Zahlen, Rechnen und Runden: Dezimalwerte mit Decimal."""

from decimal import Decimal, ROUND_HALF_UP

price = Decimal("19.99")
total = price * 3
rounded = Decimal("2.345").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(total)
print(rounded)
