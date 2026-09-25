# Übung 18 · JSON-Notizen validieren

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/18_json_csv.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`parse_notes(text)` lädt einen JSON-String. Erlaubt ist eine Liste von Dictionaries, die jeweils genau die Felder `title` und `text` mit String-Werten besitzen. Die Strings dürfen leer sein. Bei ungültiger Syntax oder Struktur muss `ValueError` entstehen. Eine leere Liste ist gültig.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [18_json_csv.py](18_json_csv.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 18
```

## Ein kleiner Hinweis

JSONDecodeError ist eine Unterklasse von ValueError. Prüfe danach den äußeren Typ und jedes Element.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
