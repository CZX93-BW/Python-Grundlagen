# 05 · Eingaben lesen und prüfen

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](04_bool_none.md) · [Nächstes Kapitel](06_bedingungen.md)

**Stufe:** Grundlage  
**Suchbegriffe:** input Terminal Konsole int strip validieren while try except Eingabe

## Wozu brauche ich das?

`input()` hält dein Programm an, bis du etwas eingibst und Enter drückst. Das Ergebnis ist immer ein String. Trenne deshalb drei Schritte: lesen, umwandeln und fachlich prüfen.

## Erst verstehen

Eine **Validierung** prüft, ob eine Eingabe zu den Anforderungen passt. Der Text "-3" lässt sich in eine Zahl umwandeln, kann als Alter aber trotzdem ungültig sein. Die Beispiele erwarten echte Eingaben im Terminal; die angezeigten Prüfausgaben wurden mit den jeweils genannten Eingaben erzeugt.

## Fall 1: Eine einfache Texteingabe

Du möchtest jemanden begrüßen.

```python
name = input("Name: ").strip()
if name:
    print(f"Hallo {name}!")
else:
    print("Bitte einen Namen eingeben.")
```

**Für diese Ausgabe nacheinander eingeben:**

```text
 Basti
```

Bei automatischer Prüfung werden Eingaben nicht vom Terminal mit angezeigt; die Aufforderungen können deshalb direkt nebeneinander stehen.

**Erwartete Ausgabe:**

```text
Name: Hallo Basti!
```

**Schritt für Schritt:**

1. Der Text in `input()` ist die Aufforderung.
2. `strip()` entfernt äußere Leerzeichen.
3. Die Bedingung unterscheidet einen gefüllten Namen von einer leeren Eingabe.

[Beispieldatei öffnen](../beispiele/05_eingaben/fall_01.py)

```powershell
python ./beispiele/05_eingaben/fall_01.py
```

## Fall 2: Eine Zahl mit Fehlermeldung

Ungültiger Text soll nicht das ganze Programm abbrechen.

```python
raw_age = input("Alter: ")
try:
    age = int(raw_age)
except ValueError:
    print("Bitte eine ganze Zahl eingeben.")
else:
    if age < 0:
        print("Das Alter darf nicht negativ sein.")
    else:
        print(f"Gespeichert: {age}")
```

**Für diese Ausgabe nacheinander eingeben:**

```text
abc
```

Bei automatischer Prüfung werden Eingaben nicht vom Terminal mit angezeigt; die Aufforderungen können deshalb direkt nebeneinander stehen.

**Erwartete Ausgabe:**

```text
Alter: Bitte eine ganze Zahl eingeben.
```

**Schritt für Schritt:**

1. `try` versucht die Umwandlung.
2. `except ValueError` behandelt genau den Fehler für einen ungeeigneten Zahlenwert.
3. `else` läuft, wenn die Umwandlung geklappt hat. Danach wird die Bedeutung des Wertes geprüft. Kapitel 16 erklärt Fehlerbehandlung genauer.

[Beispieldatei öffnen](../beispiele/05_eingaben/fall_02.py)

```powershell
python ./beispiele/05_eingaben/fall_02.py
```

## Fall 3: Bis zur gültigen Eingabe nachfragen

Du möchtest positive Stückzahlen annehmen und auch abbrechen können.

```python
while True:
    raw_value = input("Menge oder q: ").strip()
    if raw_value.casefold() == "q":
        print("Abgebrochen.")
        break
    try:
        quantity = int(raw_value)
    except ValueError:
        print("Keine ganze Zahl.")
        continue
    if quantity <= 0:
        print("Die Menge muss positiv sein.")
        continue
    print(f"Menge: {quantity}")
    break
```

**Für diese Ausgabe nacheinander eingeben:**

```text
abc
0
3
```

Bei automatischer Prüfung werden Eingaben nicht vom Terminal mit angezeigt; die Aufforderungen können deshalb direkt nebeneinander stehen.

**Erwartete Ausgabe:**

```text
Menge oder q: Keine ganze Zahl.
Menge oder q: Die Menge muss positiv sein.
Menge oder q: Menge: 3
```

**Schritt für Schritt:**

1. `while True` wiederholt die Eingabe bis zum bewussten Ausstieg.
2. `continue` startet den nächsten Versuch.
3. `break` verlässt die Schleife bei Erfolg oder bei q. Kapitel 7 führt diese Anweisungen systematisch ein.

[Beispieldatei öffnen](../beispiele/05_eingaben/fall_03.py)

```powershell
python ./beispiele/05_eingaben/fall_03.py
```

## Typische Stolperstellen

`int(input(...))` ohne Fehlerbehandlung ist nur bei garantiert gültigen Eingaben sinnvoll. `isdigit()` deckt nicht alle Umwandlungsfälle ab, etwa negative Zahlen. Verwende niemals `eval()` zum Auswerten beliebiger Eingaben. Ohne Terminal kann `input()` einen `EOFError` auslösen.

## Selbst anwenden

[Übung 05](../90_uebungen/05_eingaben.md) · [Starterdatei](../90_uebungen/05_eingaben.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/functions.html#input)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
