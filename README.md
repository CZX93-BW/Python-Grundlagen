# Dein Python-Nachschlagewerk

Eine persönliche Wissenssammlung zum Lernen und Nachschlagen. Du findest einfache Erklärungen, kleine ausführbare Beispiele, typische Fehler und eigene Übungen. Die Sprache ist Deutsch; Namen und Docstrings im Code sind überwiegend Englisch, damit du die üblichen Python-Konventionen kennenlernst.

**Beginne hier:** [Einrichtung unter Windows](00_start/SETUP_WINDOWS.md) · [Lernpfad](00_start/LERNPFAD.md) · [Nachschlagindex](INDEX.md) · [Professionelles Projekt aufsetzen](00_start/PROJEKTLEITFADEN.md)

## Schnell etwas finden

- Öffne `START_HIER.html` per Doppelklick für die durchsuchbare Offline-Leseansicht. Internet und Installation sind dafür nicht nötig. Nach eigenen Markdown-Änderungen kannst du sie mit `python ./werkzeuge/handbuch_bauen.py` aktualisieren.
- In VS Code: `Ctrl+P` sucht Dateien; `Ctrl+Shift+F` durchsucht Inhalte. Die Markdown-Vorschau öffnest du mit `Ctrl+Shift+V`.
- Nutze den [Index nach typischen Fragen](INDEX.md), wenn du den Fachbegriff noch nicht kennst.
- Im Terminal: `python ./werkzeuge/suche.py "Datei lesen"`. Mehrere Suchwörter müssen im Dokument vorkommen. Lösungen werden dabei standardmäßig ausgeblendet.

## Was du bekommst

| Ordner/Datei | Inhalt |
| --- | --- |
| `00_start/` | Einrichtung, Lernpfad, Projektleitfaden und Checkliste |
| `kapitel/` | 30 Themen mit je drei erläuterten Fällen |
| `beispiele/` | 90 separat ausführbare Beispieldateien und ein kleines Import-Hilfsmodul |
| `80_praxis/notizen/` | Vollständiges Notizprogramm auf Basis deiner ursprünglichen Übung |
| `85_projektvorlage/` | Kopierbares Python-Projekt mit src-Struktur, Tests und Werkzeugkonfiguration |
| `90_uebungen/` | 30 Aufgaben samt Starterdateien zum selbstständigen Lösen |
| `91_loesungen/` | 30 getrennte, erklärte Musterlösungen |
| `95_tests/` | Gemeinsame Prüffälle für Aufgaben und Musterlösungen |
| `99_archiv/` | Dein ursprünglicher Export und die ursprüngliche Notizübung |
| `werkzeuge/` | Suche, Übungsprüfung, Beispielprüfung und Erstellung der Offline-Ansicht |
| `FEHLERHILFE.md` | Häufige Fehlermeldungen und konkrete erste Prüfschritte |
| `GLOSSAR.md` | Fachbegriffe in einfachen Worten |
| `SPICKZETTEL.md` | Kurze Syntax-Erinnerung |

## Ein Thema bearbeiten

1. Lies im Kapitel zuerst „Wozu brauche ich das?“ und „Erst verstehen“.
2. Schau dir einen Fall an. Versuche die Ausgabe vorherzusagen.
3. Starte die verlinkte Beispieldatei und vergleiche die Ausgabe.
4. Ändere selbst einen Wert und erkläre dir, warum sich das Ergebnis ändert.
5. Bearbeite die zugehörige Aufgabe unter `90_uebungen`.
6. Prüfe deine Aufgabe, zum Beispiel Nummer 8:

```powershell
python ./werkzeuge/uebung_pruefen.py 08
```

Die Starterdateien enthalten absichtlich Platzhalter. Zu Beginn schlagen ihre Tests fehl. Das ist erwartetes Verhalten, kein Installationsfehler. Erst nach deinem eigenen Versuch liest du bei Bedarf die gleich nummerierte Datei in `91_loesungen`.

## Für neue Projekte

Folge dem [Projektleitfaden](00_start/PROJEKTLEITFADEN.md). Kopiere `85_projektvorlage` in einen **neuen** Projektordner. Die Lernsammlung und deine tatsächlichen Anwendungen bleiben damit getrennt. Die Vorlage benötigt für ihre Entwicklungswerkzeuge zusätzliche Pakete; die Kapitel, Übungen und das Notizprogramm brauchen nur die Standardbibliothek.

## Umfang und Grenzen

Stand: 25.09.2026. Die Beispiele wurden mit Python 3.12.14 unter Linux ausgeführt. Die Befehle für deinen Alltag sind für Windows/PowerShell formuliert. Eine echte Ausführung unter Windows wurde hier nicht durchgeführt. Mindestversion für diese Ausgabe ist Python 3.12. Neuere Versionen sollten für die verwendeten Grundlagen funktionieren, sind aber nicht automatisch durch diesen Prüflauf abgedeckt.

Die Sammlung deckt die zentralen Sprachgrundlagen und viele häufige Aufgaben ab. „Jeder denkbare Fall“ oder sämtliche Python-Pakete lassen sich nicht vollständig vorwegnehmen. Django, Flask, Datenanalyse und KI-Frameworks sind noch keine eigenen Kapitel. Die klare Erweiterungsvorlage hilft dir, solche Themen später sauber hinzuzufügen.

Deine Bezeichnung „Standardbibliothek“ meint hier ein persönliches Nachschlagewerk. Pythons eigentliche **Standardbibliothek** ist die mit Python ausgelieferte Sammlung von Modulen, beispielsweise `json`, `pathlib` und `sqlite3`.

[Erweitern](00_start/ERWEITERN.md) · [Quellen](QUELLEN.md) · [Prüfbericht](PRUEFBERICHT.md)
