# Lösung 15 · Ein importierbares Modul

[Zur Aufgabe](../90_uebungen/15_module.md) · [Zum Kapitel](../kapitel/15_module.md)

## Eine mögliche Lösung

```python
def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hallo {name}"

def main() -> None:
    """Run the terminal demo."""
    print(greet("Basti"))

if __name__ == "__main__":
    main()
```

## Warum funktioniert das?

Die Fachfunktion hat keine Ausgabe als Seiteneffekt. Erst die Oberfläche main() druckt das Ergebnis. Der geschützte Start erlaubt Importieren und direktes Ausführen derselben Datei.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 15 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
