# Python-Spickzettel

[Start](README.md) · [Ausführlicher Index](INDEX.md)

Die Beispiele sind kurze Erinnerungen. Lies beim ersten Lernen das verlinkte Kapitel mit den Sonderfällen.

| Ziel | Schreibweise | Kapitel |
| --- | --- | --- |
| Wert speichern | `name = "Basti"` | [01](kapitel/01_variablen_typen.md) |
| Wertetyp prüfen | `isinstance(value, str)` | [01](kapitel/01_variablen_typen.md) |
| Rest einer Division | `number % 2` | [02](kapitel/02_zahlen_operatoren.md) |
| Text einsetzen | `f"Hallo {name}"` | [03](kapitel/03_strings.md) |
| Äußere Leerzeichen entfernen | `text.strip()` | [03](kapitel/03_strings.md) |
| Ausschnitt | `items[start:stop]` | [03](kapitel/03_strings.md) |
| Fehlenden Wert prüfen | `value is None` | [04](kapitel/04_bool_none.md) |
| Nummer und Element | `enumerate(items, start=1)` | [07](kapitel/07_schleifen.md) |
| Element ergänzen | `items.append(value)` | [08](kapitel/08_listen.md) |
| Entfernen und zurückgeben | `items.pop(index)` | [08](kapitel/08_listen.md) |
| Neue sortierte Liste | `sorted(items)` | [08](kapitel/08_listen.md) |
| Fehlenden Schlüssel tolerieren | `data.get("key", default)` | [10](kapitel/10_dictionaries.md) |
| Dictionary durchlaufen | `for key, value in data.items():` | [10](kapitel/10_dictionaries.md) |
| Echte verschachtelte Kopie | `deepcopy(data)` nach Import | [11](kapitel/11_verschachteln_kopieren.md) |
| Funktion | `def calculate(value):` plus eingerückter Körper | [12](kapitel/12_funktionen.md) |
| Ergebnis zurückgeben | `return result` | [12](kapitel/12_funktionen.md) |
| Filtern | `[x for x in values if x > 0]` | [14](kapitel/14_comprehensions_sortieren.md) |
| Nach Feld sortieren | `sorted(items, key=lambda x: x["name"])` | [14](kapitel/14_comprehensions_sortieren.md) |
| Fehler auslösen | `raise ValueError("Ungültiger Wert")` | [16](kapitel/16_fehler.md) |
| UTF-8-Text lesen | `path.read_text(encoding="utf-8")` | [17](kapitel/17_dateien_pfade.md) |
| JSON-Text laden | `json.loads(text)` | [18](kapitel/18_json_csv.md) |
| Generatorwert liefern | `yield value` | [25](kapitel/25_iteratoren_generatoren.md) |

## Vier Regeln, die viele Fehler verhindern

1. `=` weist zu, `==` vergleicht Werte, `is None` prüft None.
2. `print()` zeigt an, `return` liefert ein Ergebnis für weiteren Code.
3. `append()` und `sort()` ändern eine Liste und geben None zurück.
4. Type Hints dokumentieren Typen; fremde Eingaben müssen trotzdem geprüft werden.
