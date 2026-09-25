# 01 · Variablen und Datentypen

[Start](../README.md) · [Index](../INDEX.md) · [Start](../README.md) · [Nächstes Kapitel](02_zahlen_operatoren.md)

**Stufe:** Grundlage  
**Suchbegriffe:** Variable Zuweisung int float str bool type isinstance None snake_case print

## Wozu brauche ich das?

Eine Variable ist ein Name, über den du einen Wert erreichst. Du kannst dir den Namen wie ein Etikett vorstellen: `name` zeigt auf den Text "Basti". Python erkennt den Datentyp des Wertes selbst. Du musst vor einer Zuweisung keinen Typ deklarieren.

## Erst verstehen

`=` weist einen Wert zu. `print()` zeigt etwas im Terminal. `type()` nennt den konkreten Typ. Ein **String** (`str`) ist Text, ein **Integer** (`int`) eine ganze Zahl, ein **Float** (`float`) eine Gleitkommazahl und ein **Boolean** (`bool`) ein Wahrheitswert. Funktionsaufrufe erkennst du an den runden Klammern.

## Fall 1: Werte speichern und anzeigen

Du möchtest Name, Alter und Lernstatus speichern.

```python
name = "Basti"
age = 32
is_learning = True
print(name)
print(age)
print(is_learning)
print(type(age).__name__)
```

**Erwartete Ausgabe:**

```text
Basti
32
True
int
```

**Schritt für Schritt:**

1. Die ersten drei Zeilen binden Namen an Werte. Text steht in Anführungszeichen, Zahlen nicht.
2. `print(name)` liest den gespeicherten Wert und zeigt ihn an.
3. `type(age).__name__` zeigt nur den Namen des Typs. Die doppelt unterstrichene Eigenschaft musst du noch nicht selbst schreiben.

[Beispieldatei öffnen](../beispiele/01_variablen_typen/fall_01.py)

```powershell
python ./beispiele/01_variablen_typen/fall_01.py
```

## Fall 2: Werte ändern und umwandeln

Ein Wert aus einem Formular liegt zunächst als Text vor.

```python
quantity_text = "3"
quantity = int(quantity_text)
quantity += 2
print(quantity)
print(str(quantity) + " Artikel")
print(isinstance(quantity, int))
```

**Erwartete Ausgabe:**

```text
5
5 Artikel
True
```

**Schritt für Schritt:**

1. `int("3")` erzeugt die ganze Zahl 3.
2. `+= 2` ist hier die Kurzform für `quantity = quantity + 2`.
3. `str()` macht daraus wieder Text. `isinstance()` prüft, ob der Wert zum angegebenen Typ gehört.

**Achte darauf:** `int("drei")` löst einen `ValueError` aus. Umwandlung kann scheitern; Kapitel 16 zeigt den Umgang damit.

[Beispieldatei öffnen](../beispiele/01_variablen_typen/fall_02.py)

```powershell
python ./beispiele/01_variablen_typen/fall_02.py
```

## Fall 3: Namen zeigen auf Werte

Du möchtest verstehen, was bei einer zweiten Zuweisung passiert.

```python
first = 10
second = first
first = 20
print(first, second)
```

**Erwartete Ausgabe:**

```text
20 10
```

**Schritt für Schritt:**

1. Beide Namen erreichen anfangs den Wert 10.
2. Die neue Zuweisung bindet nur `first` an 20.
3. `second` bleibt bei 10. Bei veränderbaren Listen musst du zwischen neuer Zuweisung und Änderung am Objekt unterscheiden; siehe Kapitel 11.

[Beispieldatei öffnen](../beispiele/01_variablen_typen/fall_03.py)

```powershell
python ./beispiele/01_variablen_typen/fall_03.py
```

## Typische Stolperstellen

Verwende sprechende Namen wie `first_name`. Python unterscheidet Groß- und Kleinschreibung. Ein vor der Zuweisung gelesener Name führt normalerweise zu `NameError`. Überschreibe eingebaute Namen wie `list`, `str` oder `input` nicht. `bool` ist technisch eine Unterklasse von `int`; `isinstance(True, int)` ist deshalb wahr.

## Selbst anwenden

[Übung 01](../90_uebungen/01_variablen_typen.md) · [Starterdatei](../90_uebungen/01_variablen_typen.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/functions.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
