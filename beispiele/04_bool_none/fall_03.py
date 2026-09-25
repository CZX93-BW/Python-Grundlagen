"""Wahrheitswerte, Vergleiche und None: Standardwerte gezielt einsetzen."""

quantity = 0
wrong_default = quantity or 10
correct_default = 10 if quantity is None else quantity
print(wrong_default)
print(correct_default)
name = ""
print(name or "Unbekannt")
