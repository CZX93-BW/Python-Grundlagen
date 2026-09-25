# Übung 22 · Eine Task-Dataclass

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/22_dataclasses_komposition.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

Erstelle eine Dataclass `Task` mit `title: str`, `done: bool = False` und `tags: list[str]`. Tags sollen ohne Argument eine eigene leere Liste pro Instanz erhalten. Keine zusätzliche Validierung nötig.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [22_dataclasses_komposition.py](22_dataclasses_komposition.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 22
```

## Ein kleiner Hinweis

Nutze `field(default_factory=list)` für das Listenfeld.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
