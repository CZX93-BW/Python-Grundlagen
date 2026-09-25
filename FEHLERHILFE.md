# Fehler schnell eingrenzen

[Start](README.md) · [Fehlerbehandlung](kapitel/16_fehler.md) · [Tests und Fehlersuche](kapitel/24_tests_logging.md)

## Lies zuerst diese drei Dinge

1. Die letzte Zeile der Meldung: Fehlertyp und Beschreibung.
2. Die letzte relevante Stelle in **deinem** Code im Traceback: Datei und Zeilennummer.
3. Die konkreten Werte, die an dieser Stelle ankommen. Prüfe bei Bedarf `type(value)` und `repr(value)`.

`repr()` macht beispielsweise unsichtbare Leerzeichen oder Zeilenumbrüche leichter erkennbar. Teile bei einer Hilfsfrage den relevanten Code, die vollständige Fehlermeldung, die erwartete Ausgabe und deine Python-Version mit. Entferne echte Zugangsdaten aus dem Beispiel.

| Fehlermeldung | Typische Bedeutung | Erste konkrete Prüfung |
| --- | --- | --- |
| `SyntaxError` | Python kann die Schreibweise nicht verstehen | Fehlt eine Klammer, ein Anführungszeichen oder ein Doppelpunkt? Auch die vorige Zeile ansehen. |
| `IndentationError` / `TabError` | Einrückung ist ungültig oder uneinheitlich | Vier Leerzeichen pro Ebene; Tabs und Leerzeichen nicht mischen. |
| `NameError` | Ein Name ist nicht bekannt | Schreibweise, Groß-/Kleinschreibung, Zuweisung und Import prüfen. |
| `UnboundLocalError` | Ein lokaler Name wird vor seiner Zuweisung gelesen | Wird der Name später in derselben Funktion zugewiesen? Parameter/Rückgabe statt versteckter globaler Änderung verwenden. |
| `TypeError` | Eine Operation passt nicht zu den Typen oder Argumenten | Stehen String und Zahl nebeneinander? Fehlt ein Funktionsargument? |
| `ValueError` | Der Typ passt grundsätzlich, der Wert ist ungeeignet | Zum Beispiel `int("abc")`; Originaleingabe mit repr() prüfen. |
| `IndexError` | Eine Position existiert nicht | Länge, 0-basierte Indizes und leere Liste prüfen. |
| `KeyError` | Ein Dictionary-Schlüssel fehlt | Schreibweise und erwartete Struktur prüfen; get() nur bei fachlich optionalen Daten nutzen. |
| `AttributeError` | Ein Objekt bietet die erwartete Eigenschaft/Methode nicht | Ist es möglicherweise None? Wurde das Ergebnis von append() statt der Liste gespeichert? |
| `FileNotFoundError` | Der verwendete Pfad wurde nicht gefunden | Aktuellen Arbeitsordner und vollständigen Pfad prüfen. |
| `PermissionError` | Zugriff ist nicht erlaubt oder Datei ist gesperrt | Richtiger Ordner? Schreibrechte? Datei durch anderes Programm geöffnet? |
| `UnicodeDecodeError` | Bytes passen nicht zur gewählten Zeichenkodierung | Dateiformat und tatsächliche Kodierung klären; nicht mit errors="ignore" Daten verschwinden lassen. |
| `JSONDecodeError` | Text ist kein gültiges JSON | Doppelte Anführungszeichen, fehlende Klammern oder Komma am Ende prüfen. |
| `ModuleNotFoundError` | Das Modul ist für diesen Interpreter nicht auffindbar | Interpreter, Installation mit python -m pip, Paketname und Startordner prüfen. |
| `ImportError` | Ein importierter Name ist nicht verfügbar | Namenskonflikt, zyklische Imports oder falsche Paketversion prüfen. |
| `ZeroDivisionError` | Division durch null | Eingabevalidierung und leere Sammlungen prüfen. |
| `RecursionError` | Zu viele verschachtelte Aufrufe | Fehlt die Abbruchbedingung oder nähert sie sich nicht dem Ende? |
| `NotImplementedError` in einer Übung | Der Starter ist noch nicht umgesetzt | Die markierte Funktion in 90_uebungen bearbeiten. |

## Ein reproduzierbares Beispiel bauen

Reduziere zuerst auf die kleinste Eingabe, bei der der Fehler noch auftritt. Entferne unabhängige Oberfläche und Dateizugriffe, wenn sie nicht Teil des Problems sind. Schreibe vor einer Änderung auf, was tatsächlich passiert und was passieren soll. Ändere anschließend gezielt eine Ursache und prüfe den betroffenen Fall erneut.

## Drei häufige Denkfehler

- „Kein Absturz“ bedeutet nicht automatisch „richtige Ausgabe“. Prüfe das Ergebnis ausdrücklich.
- Eine breite Fehlerbehandlung beseitigt keine Ursache. Sie kann den Fehler nur verstecken.
- Ein Paket in irgendeiner globalen Python-Installation hilft deinem Projekt nicht, wenn VS Code eine andere Umgebung startet.
