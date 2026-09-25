# Lösung 10 · Wörter zählen

[Zur Aufgabe](../90_uebungen/10_dictionaries.md) · [Zum Kapitel](../kapitel/10_dictionaries.md)

## Eine mögliche Lösung

```python
def count_words(text: str) -> dict[str, int]:
    """Count casefolded whitespace-separated words."""
    counts = {}
    for word in text.casefold().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

## Warum funktioniert das?

`split()` ohne Argument fasst Whitespace-Trennungen passend zusammen und erzeugt bei leerem Text keine leeren Wörter. Die ausdrücklich festgelegte Satzzeichenregel verhindert unklare Erwartungen.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 10 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
