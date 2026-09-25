# Praxisprojekt: deine Notizen

[Start](../../README.md) · [Erklärung zu CRUD](../../kapitel/30_notizen_crud.md)

Dieses Projekt führt deine Originalübung weiter. Du kannst Notizen anlegen, anzeigen, über ihre vollständige ID ändern und löschen. Jede erfolgreiche Änderung wird in einer JSON-Datei gespeichert. Es benötigt nur Python und keine zusätzlich installierten Pakete.

## Starten

Aus dem Hauptordner des Nachschlagewerks:

```powershell
python ./80_praxis/notizen/main.py
```

Die Daten liegen danach in `80_praxis/notizen/data/notes.json`. Der Pfad bezieht sich auf die Skriptdatei und ist deshalb vom Startordner unabhängig. Mit einer eigenen Datei:

```powershell
python ./80_praxis/notizen/main.py --file ./meine-notizen.json
```

Dieser ausdrücklich übergebene relative Pfad bezieht sich auf deinen aktuellen Terminalordner.

## Dateien verstehen

| Datei | Aufgabe |
| --- | --- |
| `main.py` | Menü, Eingaben, Anzeige und verständliche Fehlermeldungen |
| `service.py` | Daten prüfen, Notizen anlegen, suchen, ändern und löschen |
| `storage.py` | JSON lesen und vollständig geschriebenen Inhalt speichern |
| `tests/test_notes.py` | Verhalten, Grenzfälle und Dateifehler prüfen |

Lies zuerst `service.py`, dann `main.py` und zuletzt `storage.py`. Die Speichertechnik ist ein Aufbauthema. Die kleinen Funktionen aus Kapitel 30 sind der einfachere Einstieg.

## Warum diese Änderungen?

1. Das Original verwendet für Änderung und Löschung immer Position 0. Hier entscheidet eine eindeutige ID, welche Notiz gemeint ist.
2. Die Fachfunktionen lesen nicht selbst per input(). Tests können Werte direkt übergeben.
3. Titel und Text werden vor der Änderung geprüft. Ein Fehler hinterlässt keine halb geänderte Notiz.
4. Die Oberfläche bearbeitet zunächst eine Kandidatenliste. Erst nach erfolgreichem Speichern übernimmt sie diese als aktuellen Stand.
5. Eine beschädigte vorhandene JSON-Datei wird nicht als leeres Notizbuch behandelt. Das Programm beendet den Start mit einer Meldung.
6. Beim Speichern wird eine temporäre Datei im selben Ordner vollständig geschrieben und danach die Zieldatei ersetzt. Dadurch wird das Risiko einer teilweise geschriebenen Zieldatei vermindert.

## Prüfen

```powershell
python -m unittest discover -s ./80_praxis/notizen/tests -v
```

Die Tests verwenden temporäre Ordner und keine persönlichen Notizdateien.

## Bewusste Grenzen

Das ist ein Lernprojekt für eine lokal laufende Instanz. Es hat keine Anmeldung, keine Synchronisierung und keine Konfliktlösung für mehrere gleichzeitige Prozesse. IDs werden vollständig angezeigt, damit keine Abkürzung mehrdeutig ist. Das Ersetzen einer Datei ist keine Garantie gegen jeden Stromausfall und kein Ersatz für Backups. Für konkurrierende Zugriffe ist eine Datenbank mit passendem Transaktionskonzept sinnvoll.
