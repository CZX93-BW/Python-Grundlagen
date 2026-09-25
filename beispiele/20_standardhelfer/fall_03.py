"""Zählen, gruppieren und Muster erkennen: Ein einfaches Textformat prüfen."""

import re

pattern = r"[A-Z]{2}-[0-9]{3}"
print(re.fullmatch(pattern, "AB-123") is not None)
print(re.fullmatch(pattern, "AB-123-extra") is not None)
print(re.findall(r"[0-9]+", "Bestellung 12 enthält 3 Teile"))
