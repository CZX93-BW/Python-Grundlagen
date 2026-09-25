"""Zahlen, Rechnen und Runden: Gleitkommazahlen vergleichen."""

import math

result = 0.1 + 0.2
print(result)
print(result == 0.3)
print(math.isclose(result, 0.3))
print(f"{result:.2f}")
print(round(2.5), round(3.5))
