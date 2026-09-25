# 20 · Zählen, gruppieren und Muster erkennen

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](19_datum_zufall.md) · [Nächstes Kapitel](21_klassen.md)

**Stufe:** Aufbau  
**Suchbegriffe:** collections Counter defaultdict deque re regex regulärer Ausdruck fullmatch findall

## Wozu brauche ich das?

Die Standardbibliothek bietet nützliche Bausteine für häufige Aufgaben. Du musst Zählen, Warteschlangen oder einfache Textmuster nicht immer neu erfinden. Verwende diese Hilfen, sobald ihre Bedeutung für dich klar ist.

## Erst verstehen

`Counter` zählt Vorkommen. `defaultdict` erzeugt fehlende Anfangswerte über eine Funktion. `deque` ist für Einfügen und Entfernen an beiden Enden geeignet. Ein regulärer Ausdruck beschreibt ein Textmuster.

## Fall 1: Häufigkeiten zählen und Daten gruppieren

Du möchtest Wörter zählen und Namen nach Anfangsbuchstaben ordnen.

```python
from collections import Counter, defaultdict

counts = Counter(["Apfel", "Birne", "Apfel"])
print(counts["Apfel"], counts["Kiwi"])
groups = defaultdict(list)
for name in ["Ada", "Anna", "Basti"]:
    groups[name[0]].append(name)
print(dict(groups))
```

**Erwartete Ausgabe:**

```text
2 0
{'A': ['Ada', 'Anna'], 'B': ['Basti']}
```

**Schritt für Schritt:**

1. `Counter` liefert für einen fehlenden Wert 0.
2. `defaultdict(list)` erzeugt beim Zugriff auf einen fehlenden Schlüssel eine neue Liste.
3. Der aktuelle Name wird an die passende Gruppenliste angehängt.

**Achte darauf:** `groups.get(key)` löst die automatische Erzeugung nicht aus. Sie gilt für den Klammerzugriff.

[Beispieldatei öffnen](../beispiele/20_standardhelfer/fall_01.py)

```powershell
python ./beispiele/20_standardhelfer/fall_01.py
```

## Fall 2: Eine Warteschlange verwenden

Aufträge sollen in ihrer Eingangsreihenfolge bearbeitet werden.

```python
from collections import deque

queue = deque(["Auftrag A", "Auftrag B"])
queue.append("Auftrag C")
print(queue.popleft())
print(list(queue))
```

**Erwartete Ausgabe:**

```text
Auftrag A
['Auftrag B', 'Auftrag C']
```

**Schritt für Schritt:**

1. Neue Aufträge kommen rechts hinzu.
2. `popleft()` nimmt den ältesten Auftrag links heraus.
3. Anders als bei `list.pop(0)` müssen dafür nicht alle übrigen Elemente verschoben werden. Eine leere Warteschlange verursacht auch hier `IndexError`.

[Beispieldatei öffnen](../beispiele/20_standardhelfer/fall_02.py)

```powershell
python ./beispiele/20_standardhelfer/fall_02.py
```

## Fall 3: Ein einfaches Textformat prüfen

Eine Artikelnummer muss aus zwei Großbuchstaben und drei Ziffern bestehen.

```python
import re

pattern = r"[A-Z]{2}-[0-9]{3}"
print(re.fullmatch(pattern, "AB-123") is not None)
print(re.fullmatch(pattern, "AB-123-extra") is not None)
print(re.findall(r"[0-9]+", "Bestellung 12 enthält 3 Teile"))
```

**Erwartete Ausgabe:**

```text
True
False
['12', '3']
```

**Schritt für Schritt:**

1. `[A-Z]{2}` verlangt genau zwei Zeichen aus A bis Z.
2. `[0-9]{3}` verlangt drei ASCII-Ziffern. `fullmatch()` prüft den gesamten Text.
3. `findall()` findet alle passenden Teilstücke; `+` bedeutet mindestens ein Zeichen. Das `r` vor einem String lässt Backslashes weitgehend wörtlich stehen.

[Beispieldatei öffnen](../beispiele/20_standardhelfer/fall_03.py)

```powershell
python ./beispiele/20_standardhelfer/fall_03.py
```

## Typische Stolperstellen

Reguläre Ausdrücke werden schnell unleserlich. Für reine Teilstrings reichen `in`, `startswith()` oder `split()`. Nutze ein Muster nicht als vollständige Prüfung komplexer Formate wie HTML oder E-Mail-Adressen. `re.search()` prüft ein Vorkommen, `fullmatch()` die gesamte Eingabe.

## Selbst anwenden

[Übung 20](../90_uebungen/20_standardhelfer.md) · [Starterdatei](../90_uebungen/20_standardhelfer.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/collections.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
