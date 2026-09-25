# 07 · Schleifen und Wiederholungen

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](06_bedingungen.md) · [Nächstes Kapitel](08_listen.md)

**Stufe:** Grundlage  
**Suchbegriffe:** for while range enumerate zip break continue else Endlosschleife

## Wozu brauche ich das?

Einen Ablauf für mehrere Werte zu wiederholen ist eine häufige Aufgabe. Verwende `for`, wenn du über vorhandene Elemente oder einen Zahlenbereich gehen möchtest. Verwende `while`, wenn eine Bedingung bestimmt, wie lange es weitergeht.

## Erst verstehen

Ein einzelner Durchgang heißt **Iteration**. `break` beendet die innerste Schleife. `continue` überspringt den Rest des aktuellen Durchgangs. Verschachtelte Schleifen durchlaufen für jeden äußeren Durchgang die innere Schleife erneut.

## Fall 1: Elemente und Positionen durchgehen

Du möchtest eine nummerierte Liste anzeigen.

```python
fruits = ["Apfel", "Birne", "Kiwi"]
for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)
print(list(range(2, 8, 2)))
```

**Erwartete Ausgabe:**

```text
1 Apfel
2 Birne
3 Kiwi
[2, 4, 6]
```

**Schritt für Schritt:**

1. `enumerate()` liefert jeweils eine Nummer und ein Element. Die Nummerierung darf bei 1 beginnen.
2. Die eigentlichen Listenindizes beginnen weiterhin bei 0.
3. `range(2, 8, 2)` liefert 2, 4 und 6. Die obere Grenze 8 ist ausgeschlossen.

[Beispieldatei öffnen](../beispiele/07_schleifen/fall_01.py)

```powershell
python ./beispiele/07_schleifen/fall_01.py
```

## Fall 2: Wiederholen und gezielt überspringen

Du möchtest nur bestimmte Werte verarbeiten.

```python
number = 0
while number < 5:
    number += 1
    if number == 2:
        continue
    if number == 4:
        break
    print(number)
```

**Erwartete Ausgabe:**

```text
1
3
```

**Schritt für Schritt:**

1. Der Zähler wird vor jeder Prüfung erhöht.
2. Bei 2 springt das Programm zum Schleifenanfang.
3. Bei 4 verlässt `break` die Schleife. Ohne Fortschritt im Zähler könnte eine Endlosschleife entstehen.

[Beispieldatei öffnen](../beispiele/07_schleifen/fall_02.py)

```powershell
python ./beispiele/07_schleifen/fall_02.py
```

## Fall 3: Suchen und zusammengehörige Listen verbinden

Du suchst einen Wert und kombinierst anschließend Namen mit Punkten.

```python
for number in [1, 3, 5]:
    if number % 2 == 0:
        print("Gerade Zahl gefunden")
        break
else:
    print("Keine gerade Zahl gefunden")

for name, score in zip(["Ada", "Basti"], [9, 8], strict=True):
    print(name, score)
```

**Erwartete Ausgabe:**

```text
Keine gerade Zahl gefunden
Ada 9
Basti 8
```

**Schritt für Schritt:**

1. Das `else` gehört zur Schleife und läuft nur, wenn sie regulär ohne `break` endet.
2. `zip()` verbindet jeweils Elemente derselben Position.
3. `strict=True` meldet unterschiedlich lange Eingaben mit `ValueError`; ohne diese Option würde `zip()` bei der kürzesten Eingabe aufhören.

[Beispieldatei öffnen](../beispiele/07_schleifen/fall_03.py)

```powershell
python ./beispiele/07_schleifen/fall_03.py
```

## Typische Stolperstellen

Entferne während einer Iteration über eine Liste nicht unbedacht Elemente derselben Liste: Positionen verschieben sich. Erzeuge lieber eine neue gefilterte Liste. Bei einer leeren Sammlung läuft der for-Block kein einziges Mal. Mit `Ctrl+C` kannst du eine laufende Endlosschleife im Terminal normalerweise abbrechen.

## Selbst anwenden

[Übung 07](../90_uebungen/07_schleifen.md) · [Starterdatei](../90_uebungen/07_schleifen.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/controlflow.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
