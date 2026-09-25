# Einstieg mit VS Code und PowerShell

[Start](../README.md) · [Projektleitfaden](PROJEKTLEITFADEN.md)

## 1. Ordner öffnen

Entpacke die ZIP-Datei. Öffne in VS Code den Ordner `python-nachschlagewerk`, in dem `README.md` liegt. Öffne über das Terminalmenü ein PowerShell-Terminal. Alle relativen Befehle in den Kapiteln gehen von diesem Hauptordner aus.

## 2. Python prüfen

```powershell
py --version
python --version
```

Mindestens einer der beiden Befehle muss den gewünschten Python-Interpreter ab Version 3.12 finden. Dass ein Befehl fehlt, ist nicht automatisch ein Problem. Wenn beide fehlen, installiere Python von [python.org](https://www.python.org/downloads/windows/) und öffne danach ein neues Terminal. Nutze in VS Code die Python-Erweiterung von Microsoft und wähle den passenden Interpreter. Die genaue Installationsoberfläche kann sich ändern; entscheidend ist der anschließend tatsächlich gestartete Interpreter.

## 3. Virtuelle Umgebung anlegen

```powershell
py -m venv .venv
```

Wenn bei dir nur `python` verfügbar ist: `python -m venv .venv`. Eine virtuelle Umgebung hält projektbezogene Python-Pakete getrennt. Sie wird pro Projekt angelegt und nicht ins Repository aufgenommen.

Du kannst sie aktivieren:

```powershell
.\.venv\Scripts\Activate.ps1
```

Falls PowerShell die Aktivierung blockiert, musst du für dieses Nachschlagewerk keine Ausführungsrichtlinie ändern. Verwende direkt den Interpreter:

```powershell
.\.venv\Scripts\python.exe ./beispiele/01_variablen_typen/fall_01.py
```

In einem aktivierten Terminal genügt:

```powershell
python ./beispiele/01_variablen_typen/fall_01.py
```

## 4. Interpreter im Editor auswählen

Öffne die Befehlspalette mit `Ctrl+Shift+P`, suche `Python: Select Interpreter` und wähle die `.venv` dieses Ordners. Kontrolliere anschließend im Terminal:

```powershell
python -c "import sys; print(sys.executable)"
```

Die Ausgabe soll zur beabsichtigten Umgebung passen. Bei Verwendung des expliziten `.venv`-Pfads ist diese Zuordnung eindeutig. Die Auswahl im Editor und bereits geöffnete Terminalprozesse können voneinander abweichen; öffne bei Bedarf ein neues Terminal.

## 5. Lesen, ausprobieren, üben

Öffne [Kapitel 1](../kapitel/01_variablen_typen.md). Die Vorschau erreichst du mit `Ctrl+Shift+V`. Ein Beispiel mit `input()` braucht ein interaktives Terminal. Starte es über den angegebenen Python-Befehl, statt es in ein reines Ausgabefenster zu schicken.

Du musst für Kapitel und Übungen nichts per pip installieren. In `85_projektvorlage` ist das anders: Dort gehören optionale Entwicklungswerkzeuge zum professionellen Ablauf.

## 6. Gewünschtes Verhalten prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 01
python ./werkzeuge/beispiele_pruefen.py
```

Die erste Übung schlägt vor deiner Bearbeitung absichtlich fehl. Die Beispielprüfung führt die 90 Demo-Dateien mit vorbereiteten Eingaben aus. Sie benötigt kein Internet.

## Häufige Verwechslungen

| Beobachtung | Erste Prüfung |
| --- | --- |
| Python findet die Datei nicht | Liegt das Terminal im Hauptordner? `Get-Location` zeigt ihn. |
| Ein Paket wurde installiert, der Import scheitert trotzdem | Nutzt pip denselben Interpreter? Verwende `python -m pip`, nicht ein beliebiges `pip`. |
| Doppelklick lässt das Terminal sofort verschwinden | Starte die Datei im bereits geöffneten VS-Code-Terminal. |
| Ein Lernbeispiel erwartet Enter | Das ist die input()-Funktion; führe es interaktiv aus. |
| Umlaute sehen falsch aus | Dateien als UTF-8 speichern; bei Bedarf `python -X utf8 datei.py` verwenden. |
