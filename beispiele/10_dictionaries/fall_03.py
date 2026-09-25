"""Dictionaries und Schlüssel-Wert-Paare: Fehlende Werte und Löschen."""

settings = {"theme": None}
print(settings.get("theme", "light"))
print(settings.get("language", "de"))
settings.setdefault("language", "de")
removed = settings.pop("theme", "Nicht vorhanden")
print(removed)
print(settings)
