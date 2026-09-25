# Lösungen

[Start](../README.md) · [Lernpfad](../00_start/LERNPFAD.md)

Die gleichen Nummern verbinden Kapitel, Aufgabe, Starterdatei und Lösung. Die ersten Aufgaben sind klein. Ab Klasse/Dateien kommen mehr Schritte dazu. Die anspruchsvollen Aufgaben 25, 26, 27 und 29 darfst du zunächst überspringen.

| Nummer | Thema | Stufe |
| --- | --- | --- |
| 01 | [Begrüßung zusammensetzen](01_variablen_typen.md) | Leicht |
| 02 | [Minuten aufteilen](02_zahlen_operatoren.md) | Leicht |
| 03 | [Suchtext normalisieren](03_strings.md) | Leicht |
| 04 | [Fehlende Werte ergänzen](04_bool_none.md) | Leicht |
| 05 | [Positive Zahl aus Text lesen](05_eingaben.md) | Leicht |
| 06 | [Punktestand einordnen](06_bedingungen.md) | Leicht |
| 07 | [Gerade Zahlen summieren](07_schleifen.md) | Leicht |
| 08 | [Doppelte Einträge entfernen](08_listen.md) | Leicht |
| 09 | [Gemeinsame Fähigkeiten finden](09_tupel_sets.md) | Leicht |
| 10 | [Wörter zählen](10_dictionaries.md) | Leicht |
| 11 | [Eine unabhängige Notizkopie](11_verschachteln_kopieren.md) | Mittel |
| 12 | [Durchschnitt berechnen](12_funktionen.md) | Leicht |
| 13 | [Tags ohne geteilten Standardwert](13_parameter_scope.md) | Mittel |
| 14 | [Personen filtern und sortieren](14_comprehensions_sortieren.md) | Mittel |
| 15 | [Ein importierbares Modul](15_module.md) | Mittel |
| 16 | [Einen Port validieren](16_fehler.md) | Mittel |
| 17 | [Nicht leere Zeilen lesen](17_dateien_pfade.md) | Mittel |
| 18 | [JSON-Notizen validieren](18_json_csv.md) | Mittel |
| 19 | [Datumsabstand bestimmen](19_datum_zufall.md) | Mittel |
| 20 | [Artikelnummer prüfen](20_standardhelfer.md) | Mittel |
| 21 | [Ein Zähler als Klasse](21_klassen.md) | Mittel |
| 22 | [Eine Task-Dataclass](22_dataclasses_komposition.md) | Mittel |
| 23 | [Eine Funktion dokumentieren](23_typen_dokumentation.md) | Mittel |
| 24 | [Einen Fehler mit Tests absichern](24_tests_logging.md) | Mittel |
| 25 | [Gerade Zahlen als Generator](25_iteratoren_generatoren.md) | Anspruchsvoll |
| 26 | [Einen Rückgabewert dekorieren](26_decorators_kontext.md) | Anspruchsvoll |
| 27 | [Einen Kontakt in SQLite anlegen](27_sqlite.md) | Anspruchsvoll |
| 28 | [Boolesche Konfiguration lesen](28_cli_http_config.md) | Mittel |
| 29 | [Eine Coroutine schreiben](29_async_laufzeit.md) | Anspruchsvoll |
| 30 | [Notiz mit stabiler ID ändern](30_notizen_crud.md) | Mittel |

## Tests verstehen

`OK` bedeutet, dass die vorhandenen Prüffälle bestanden wurden. Das beweist nicht, dass jede denkbare Eingabe korrekt behandelt ist. `FAIL` bedeutet eine unerwartete Ausgabe; `ERROR` bedeutet meist eine ausgelöste Exception. Lies den Namen des fehlgeschlagenen Tests und die letzte Fehlermeldung.

```powershell
python ./werkzeuge/uebung_pruefen.py 01
python ./werkzeuge/uebung_pruefen.py 01 --loesung
```

Der erste Befehl prüft deine Arbeit, der zweite die Musterlösung. Die Prüffälle und Anforderungen sind identisch.
