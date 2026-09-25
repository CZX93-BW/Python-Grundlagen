# Python-Projektvorlage

Eine kleine, kopierbare Grundlage mit `src`-Struktur, Fachfunktion, CLI und Tests. Python 3.12 oder neuer; keine zusätzlichen Laufzeitabhängigkeiten. Der ausführliche Leitfaden befindet sich im Nachschlagewerk unter `00_start/PROJEKTLEITFADEN.md`.

## Einrichten unter Windows / PowerShell

Kopiere diesen Ordner für ein neues Projekt und öffne **den kopierten Ordner** in VS Code. Führe die Befehle dort aus:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m starter_app "Basti"
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Falls `py` fehlt, aber `python --version` den gewünschten Interpreter zeigt, verwende für die erste Zeile `python -m venv .venv`. Die Installation benötigt Zugriff auf einen Paketindex. Die Aktivierung der Umgebung ist für die expliziten Python-Pfade nicht nötig. Wähle in VS Code über `Python: Select Interpreter` ebenfalls die `.venv` dieser Kopie.

Die Ausgabe der Anwendung lautet `Hallo Basti!`. Für die normale Nutzung im aktivierten Terminal genügt `python -m starter_app "Basti"`. Alternativ installiert das Projekt den Terminalbefehl `python-starter`.

## Qualität prüfen

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m mypy
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Formatierung anwenden: `python -m ruff format .` im aktivierten Terminal. Automatische Korrekturen mit `ruff check --fix` immer im Diff prüfen.

## Dateien und Verantwortung

| Pfad | Zweck |
| --- | --- |
| `src/starter_app/service.py` | Fachlogik: Name prüfen und Begrüßung erzeugen |
| `src/starter_app/cli.py` | Argumente lesen, Ergebnis anzeigen, Fehlercode liefern |
| `src/starter_app/__main__.py` | Einstieg für `python -m starter_app` |
| `tests/` | Normal-, Grenz- und Fehlerfälle |
| `pyproject.toml` | Projektmetadaten, Abhängigkeiten und Werkzeugregeln |
| `.env.example` | Nur ein Beispiel für Konfigurationsdokumentation; wird nicht automatisch geladen |

## Für dein Projekt anpassen

Ändere Projektname und Beschreibung in `pyproject.toml`. Benenne das Paket `starter_app` bei Bedarf um und passe danach alle Imports sowie `[project.scripts]` an. Beginne mit einer einzigen konkreten Fachfunktion. Ergänze Ordner erst, wenn sie eine echte Aufgabe bekommen.

Die Entwicklungswerkzeuge sind bewusst ohne exakte Versionspins angegeben. Das ist eine startbare Vorlage, noch kein reproduzierbar gesperrter Release-Stand. Installiere und prüfe sie in deiner Umgebung und lege danach die tatsächlich geprüften Versionen beziehungsweise eine Lockdatei für dein eigenes Projekt fest. Der Leitfaden erklärt den Unterschied.

## Optional: installierbares Paket bauen

```powershell
.\.venv\Scripts\python.exe -m build
```

Das erzeugt Distributionsdateien in `dist/`, veröffentlicht aber nichts. Prüfe sie in einer frischen Umgebung, bevor du etwas veröffentlichst. Eine Veröffentlichung und eine Lizenzentscheidung erfolgen nicht automatisch durch diese Vorlage.
