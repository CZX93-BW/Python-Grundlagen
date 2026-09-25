# Lösung 06 · Punktestand einordnen

[Zur Aufgabe](../90_uebungen/06_bedingungen.md) · [Zum Kapitel](../kapitel/06_bedingungen.md)

## Eine mögliche Lösung

```python
def classify_score(points: int) -> str:
    """Classify a score from zero to one hundred."""
    if not 0 <= points <= 100:
        raise ValueError("Punkte müssen zwischen 0 und 100 liegen")
    if points >= 90:
        return "sehr gut"
    if points >= 60:
        return "bestanden"
    return "weiter üben"
```

## Warum funktioniert das?

Die Bereichsprüfung kommt vor der Zuordnung. Absteigende Grenzwerte verhindern, dass 95 Punkte bereits vom allgemeineren >=60-Fall abgefangen werden.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 06 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
