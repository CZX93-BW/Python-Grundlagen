# Übung 28 · Boolesche Konfiguration lesen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/28_cli_http_config.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`parse_bool(text)` akzeptiert nach strip() und casefold() die wahren Werte `true`, `1`, `yes` und die falschen Werte `false`, `0`, `no`. Andere Texte lösen ValueError aus. Gib echte Boolean-Werte zurück.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [28_cli_http_config.py](28_cli_http_config.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 28
```

## Ein kleiner Hinweis

Ein nicht leerer String ist auch dann truthy, wenn er "false" lautet.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
