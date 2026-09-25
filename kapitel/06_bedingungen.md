# 06 · Entscheidungen mit if und match

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](05_eingaben.md) · [Nächstes Kapitel](07_schleifen.md)

**Stufe:** Grundlage  
**Suchbegriffe:** if elif else match case switch Einrückung Bedingung ternär

## Wozu brauche ich das?

Mit einer Verzweigung führst du Code nur unter bestimmten Bedingungen aus. Python erkennt die zusammengehörigen Zeilen an ihrer Einrückung. Nutze konsequent vier Leerzeichen pro Ebene.

## Erst verstehen

`if` prüft zuerst, `elif` prüft weitere Fälle und `else` ist der Restfall. Nur der erste passende Zweig einer solchen Kette läuft. Mehrere unabhängige `if`-Anweisungen können dagegen alle ausgeführt werden.

## Fall 1: Bereiche unterscheiden

Ein Punktestand soll eine passende Rückmeldung erhalten.

```python
points = 75
if points >= 90:
    print("Sehr gut")
elif points >= 60:
    print("Bestanden")
else:
    print("Weiter üben")
```

**Erwartete Ausgabe:**

```text
Bestanden
```

**Schritt für Schritt:**

1. Die strengste Bedingung steht zuerst.
2. Bei 75 ist die erste Bedingung falsch und die zweite wahr.
3. Nach dem passenden Zweig werden die restlichen Zweige übersprungen.

**Achte darauf:** Würdest du `>= 60` zuerst prüfen, erreichten auch 95 Punkte diesen Zweig und nie den Zweig für "Sehr gut".

[Beispieldatei öffnen](../beispiele/06_bedingungen/fall_01.py)

```powershell
python ./beispiele/06_bedingungen/fall_01.py
```

## Fall 2: Einen von zwei Werten auswählen

Du brauchst nur eine kurze Entscheidung für einen Wert.

```python
is_online = False
status = "Online" if is_online else "Offline"
print(status)
```

**Erwartete Ausgabe:**

```text
Offline
```

**Schritt für Schritt:**

1. Lies den Ausdruck als: "Online, wenn is_online wahr ist, sonst Offline".
2. Das Ergebnis wird in `status` gespeichert.
3. Für längere Abläufe bleibt ein normaler if-Block leichter lesbar.

[Beispieldatei öffnen](../beispiele/06_bedingungen/fall_02.py)

```powershell
python ./beispiele/06_bedingungen/fall_02.py
```

## Fall 3: Feste Befehle mit match behandeln

Ein Menü kennt mehrere eindeutige Befehle.

```python
command = "list"
match command:
    case "list" | "show":
        print("Einträge anzeigen")
    case "quit":
        print("Beenden")
    case _:
        print("Unbekannter Befehl")
```

**Erwartete Ausgabe:**

```text
Einträge anzeigen
```

**Schritt für Schritt:**

1. `match` vergleicht den Befehl mit Mustern. Hier sind das feste Texte.
2. `|` verbindet alternative Muster.
3. `_` passt als letzter Restfall auf alles. `match` ist seit Python 3.10 verfügbar.

**Achte darauf:** Ein nackter Name nach `case`, etwa `case expected:`, bindet normalerweise einen Namen und vergleicht nicht automatisch mit einer vorhandenen Variablen.

[Beispieldatei öffnen](../beispiele/06_bedingungen/fall_03.py)

```powershell
python ./beispiele/06_bedingungen/fall_03.py
```

## Typische Stolperstellen

Nach `if`, `elif`, `else`, `match` und `case` steht ein Doppelpunkt. Mische keine Tabs und Leerzeichen. Verwende `==` zum Vergleichen. Ein leerer Block benötigt vorübergehend `pass`; `pass` führt keine Aktion aus.

## Selbst anwenden

[Übung 06](../90_uebungen/06_bedingungen.md) · [Starterdatei](../90_uebungen/06_bedingungen.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/controlflow.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
