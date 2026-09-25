# 04 · Wahrheitswerte, Vergleiche und None

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](03_strings.md) · [Nächstes Kapitel](05_eingaben.md)

**Stufe:** Grundlage  
**Suchbegriffe:** bool None is gleich Vergleich and or not truthy falsy leer

## Wozu brauche ich das?

Bedingungen entscheiden, welcher Code ausgeführt wird. Sie liefern oft `True` oder `False`. `None` ist etwas anderes: Es steht für einen fehlenden oder bewusst nicht vorhandenen Wert.

## Erst verstehen

`==` vergleicht Werte, `!=` bedeutet ungleich. `is` vergleicht Objektidentität und wird vor allem als `is None` verwendet. `and`, `or` und `not` verbinden Bedingungen. Leere Sammlungen, leere Strings, null und `None` werden in Bedingungen als falsch behandelt.

## Fall 1: Bedingungen verbinden

Ein Zugang setzt Volljährigkeit und Zustimmung voraus.

```python
age = 20
has_consent = True
print(age >= 18 and has_consent)
print(age < 18 or not has_consent)
print(18 <= age < 65)
```

**Erwartete Ausgabe:**

```text
True
False
True
```

**Schritt für Schritt:**

1. `>=` bedeutet größer oder gleich.
2. Bei `and` müssen beide Bedingungen zutreffen; bei `or` genügt eine.
3. Python erlaubt verkettete Vergleiche wie `18 <= age < 65`.

[Beispieldatei öffnen](../beispiele/04_bool_none/fall_01.py)

```powershell
python ./beispiele/04_bool_none/fall_01.py
```

## Fall 2: Leer und fehlend unterscheiden

Eine leere Liste kann ein gültiges Ergebnis sein; None kann "noch nicht geladen" bedeuten.

```python
items = []
result = None
print(bool(items))
print(items is None)
print(result is None)
print(bool("False"))
```

**Erwartete Ausgabe:**

```text
False
False
True
True
```

**Schritt für Schritt:**

1. `[]` ist leer, aber ein vorhandenes Listenobjekt.
2. `is None` fragt gezielt nach dem fehlenden Wert.
3. Der Text `"False"` ist nicht leer und wird deshalb als wahr ausgewertet. Text wird nicht automatisch als Wahrheitswort interpretiert.

[Beispieldatei öffnen](../beispiele/04_bool_none/fall_02.py)

```powershell
python ./beispiele/04_bool_none/fall_02.py
```

## Fall 3: Standardwerte gezielt einsetzen

Null ist ein gültiger Wert und soll nicht versehentlich ersetzt werden.

```python
quantity = 0
wrong_default = quantity or 10
correct_default = 10 if quantity is None else quantity
print(wrong_default)
print(correct_default)
name = ""
print(name or "Unbekannt")
```

**Erwartete Ausgabe:**

```text
10
0
Unbekannt
```

**Schritt für Schritt:**

1. `or` liefert einen der Operanden, nicht zwingend `True` oder `False`.
2. Deshalb ersetzt `quantity or 10` auch eine gültige 0.
3. Der bedingte Ausdruck prüft ausdrücklich `None`. Beim Namen kann das Ersetzen eines leeren Strings dagegen erwünscht sein.

[Beispieldatei öffnen](../beispiele/04_bool_none/fall_03.py)

```powershell
python ./beispiele/04_bool_none/fall_03.py
```

## Typische Stolperstellen

Verwende `==` für gleiche Werte und `is None` für None. Eine Identitätsprüfung wie `name is "Basti"` ist kein verlässlicher Textvergleich. `and` und `or` werten den zweiten Ausdruck nur aus, wenn er noch gebraucht wird; das heißt Kurzschlussauswertung.

## Selbst anwenden

[Übung 04](../90_uebungen/04_bool_none.md) · [Starterdatei](../90_uebungen/04_bool_none.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/stdtypes.html#truth-value-testing)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
