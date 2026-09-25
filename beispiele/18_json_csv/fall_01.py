"""JSON und CSV lesen und schreiben: Python-Daten und JSON-Text umwandeln."""

import json

person = {"name": "Jörg", "active": True, "phone": None}
text = json.dumps(person, ensure_ascii=False, sort_keys=True)
print(text)
restored = json.loads(text)
print(restored["name"])
print(restored["phone"] is None)
