# 03 · Texte bearbeiten und formatieren

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](02_zahlen_operatoren.md) · [Nächstes Kapitel](04_bool_none.md)

**Stufe:** Grundlage  
**Suchbegriffe:** String str strip split join replace slicing f-string lower casefold startswith find Unicode

## Wozu brauche ich das?

Textverarbeitung brauchst du bei Eingaben, Dateinamen und Suchfunktionen. Strings sind unveränderbar: Methoden geben normalerweise einen neuen Text zurück. Der ursprüngliche String wird dadurch nicht umgeschrieben.

## Erst verstehen

Ein **Index** ist eine Position und beginnt bei 0. Ein **Slice** ist ein Ausschnitt mit `text[start:stop]`; die Endposition gehört nicht mehr dazu. Eine **Methode** ist eine Funktion, die du über einen Wert aufrufst, zum Beispiel `text.strip()`.

## Fall 1: Eingaben säubern und vergleichen

Du möchtest einen Suchbegriff unabhängig von Großschreibung vergleichen.

```python
raw_name = "  Straße  "
clean_name = raw_name.strip()
print(clean_name)
print(clean_name.casefold() == "STRASSE".casefold())
print(raw_name == clean_name)
```

**Erwartete Ausgabe:**

```text
Straße
True
False
```

**Schritt für Schritt:**

1. `strip()` entfernt äußere Leerzeichen und andere äußere Whitespace-Zeichen.
2. `casefold()` eignet sich für viele Vergleiche ohne Groß-/Kleinschreibung; hier wird ß zu ss.
3. Der ursprüngliche Text bleibt unverändert.

**Achte darauf:** `strip("abc")` entfernt einzelne Zeichen aus dieser Zeichenmenge an den Rändern, nicht das genaue Wort "abc".

[Beispieldatei öffnen](../beispiele/03_strings/fall_01.py)

```powershell
python ./beispiele/03_strings/fall_01.py
```

## Fall 2: Aufteilen, verbinden und ersetzen

Eine kommagetrennte Eingabe soll lesbar ausgegeben werden.

```python
text = "Apfel,Birne,Kiwi"
fruits = text.split(",")
print(fruits)
print(" | ".join(fruits))
print(text.replace("Kiwi", "Mango"))
print(text.startswith("Apfel"))
```

**Erwartete Ausgabe:**

```text
['Apfel', 'Birne', 'Kiwi']
Apfel | Birne | Kiwi
Apfel,Birne,Mango
True
```

**Schritt für Schritt:**

1. `split()` macht aus einem Text eine Liste von Textteilen.
2. `join()` verbindet Strings mit einem Trenntext. Die Methode gehört zum Trenntext.
3. `replace()` erzeugt einen neuen Text. Für echte CSV-Dateien mit Anführungszeichen und Trennzeichen im Inhalt brauchst du das `csv`-Modul.

[Beispieldatei öffnen](../beispiele/03_strings/fall_02.py)

```powershell
python ./beispiele/03_strings/fall_02.py
```

## Fall 3: Ausschnitte und lesbare Ausgaben

Du möchtest Textteile auswählen und Werte in einen Satz einsetzen.

```python
language = "Python"
print(language[0], language[-1])
print(language[1:4])
print(language[::-1])
price = 12.5
print(f"{language}: {price:.2f} EUR")
print("abc".find("x"))
```

**Erwartete Ausgabe:**

```text
P n
yth
nohtyP
Python: 12.50 EUR
-1
```

**Schritt für Schritt:**

1. `0` ist das erste, `-1` das letzte Element.
2. `[1:4]` nimmt die Positionen 1, 2 und 3. Der dritte Slice-Wert ist die Schrittweite; -1 geht rückwärts.
3. Ein f-String setzt Ausdrücke in `{}` ein. `find()` liefert bei fehlendem Text -1.

**Achte darauf:** Ein direkter Zugriff außerhalb des Textes wirft `IndexError`; ein Slice darf über das Ende hinausreichen. Unicode-Zeichen können aus mehreren Codepoints bestehen: `len()` zählt keine sichtbaren Schriftzeichen im sprachlichen Sinn.

[Beispieldatei öffnen](../beispiele/03_strings/fall_03.py)

```powershell
python ./beispiele/03_strings/fall_03.py
```

## Typische Stolperstellen

`"5" + "2"` ergibt `"52"`, nicht 7. `join()` benötigt Strings. `lower()` und `casefold()` sind ähnlich, aber nicht identisch. `find()` nicht ungeprüft als Index benutzen: -1 würde auf das letzte Zeichen zugreifen.

## Selbst anwenden

[Übung 03](../90_uebungen/03_strings.md) · [Starterdatei](../90_uebungen/03_strings.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/stdtypes.html#text-sequence-type-str)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
