# 02 · Zahlen, Rechnen und Runden

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](01_variablen_typen.md) · [Nächstes Kapitel](03_strings.md)

**Stufe:** Grundlage  
**Suchbegriffe:** Addition Subtraktion Division Modulo Potenz round Decimal float Geld math

## Wozu brauche ich das?

Mit Zahlen berechnest du Mengen, Preise oder Durchschnittswerte. Welche Art von Division du verwendest, entscheidet darüber, ob du eine Gleitkommazahl, einen abgerundeten Quotienten oder einen Rest erhältst.

## Erst verstehen

`+`, `-`, `*` rechnen wie gewohnt. `/` teilt, `//` rundet den Quotienten nach unten, `%` liefert den Rest und `**` potenziert. Klammern machen die Reihenfolge klar. Ein Punkt ist das Dezimalzeichen in Python-Code.

## Fall 1: Die wichtigsten Rechenzeichen

Du verteilst sieben Gegenstände auf zwei Gruppen.

```python
print(7 + 2, 7 - 2, 7 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 3)
print(-7 // 2)
```

**Erwartete Ausgabe:**

```text
9 5 14
3.5
3
1
8
-4
```

**Schritt für Schritt:**

1. `/` liefert hier 3.5, auch eine genau aufgehende Ganzzahldivision mit `/` liefert einen Float.
2. `//` liefert 3; `%` liefert den Rest 1.
3. Bei negativen Werten wird nach unten gerundet: -3.5 wird -4, nicht -3.

[Beispieldatei öffnen](../beispiele/02_zahlen_operatoren/fall_01.py)

```powershell
python ./beispiele/02_zahlen_operatoren/fall_01.py
```

## Fall 2: Gleitkommazahlen vergleichen

Du möchtest berechnete Werte sinnvoll vergleichen.

```python
import math

result = 0.1 + 0.2
print(result)
print(result == 0.3)
print(math.isclose(result, 0.3))
print(f"{result:.2f}")
print(round(2.5), round(3.5))
```

**Erwartete Ausgabe:**

```text
0.30000000000000004
False
True
0.30
2 4
```

**Schritt für Schritt:**

1. Viele Dezimalbrüche sind binär nicht exakt darstellbar. Deshalb entsteht die sichtbare Abweichung.
2. `math.isclose()` prüft Nähe innerhalb einer Toleranz. In der Nähe von null kann ein passendes `abs_tol` nötig sein.
3. `:.2f` formatiert nur die Ausgabe. `round()` rundet bei exakten Halbwerten zur geraden Nachbarzahl.

**Achte darauf:** Die passende Toleranz hängt vom Anwendungsfall ab. Formatierung behebt keine Rechenungenauigkeit.

[Beispieldatei öffnen](../beispiele/02_zahlen_operatoren/fall_02.py)

```powershell
python ./beispiele/02_zahlen_operatoren/fall_02.py
```

## Fall 3: Dezimalwerte mit Decimal

Du willst eine einfache Preisrechnung nachvollziehbar ausführen.

```python
from decimal import Decimal, ROUND_HALF_UP

price = Decimal("19.99")
total = price * 3
rounded = Decimal("2.345").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(total)
print(rounded)
```

**Erwartete Ausgabe:**

```text
59.97
2.35
```

**Schritt für Schritt:**

1. `Decimal` bekommt hier Text, damit nicht vorher ein ungenauer Float entsteht.
2. `quantize()` legt die Dezimalstellen und die Rundungsregel ausdrücklich fest.
3. `ROUND_HALF_UP` rundet einen Halbwert vom Nullpunkt weg. Welche Regel fachlich richtig ist, muss für das konkrete Projekt feststehen.

[Beispieldatei öffnen](../beispiele/02_zahlen_operatoren/fall_03.py)

```powershell
python ./beispiele/02_zahlen_operatoren/fall_03.py
```

## Typische Stolperstellen

Division durch null verursacht `ZeroDivisionError`. `int(3.9)` schneidet Richtung null ab und ist kein normales Runden. Verwende für zusammengehörige Rechnungen passende, kompatible Zahlentypen. Bei `Decimal` gilt ebenfalls eine endliche Rechengenauigkeit.

## Selbst anwenden

[Übung 02](../90_uebungen/02_zahlen_operatoren.md) · [Starterdatei](../90_uebungen/02_zahlen_operatoren.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/decimal.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
