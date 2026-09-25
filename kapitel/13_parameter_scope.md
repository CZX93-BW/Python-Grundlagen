# 13 · Parameter, Standardwerte und Gültigkeitsbereiche

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](12_funktionen.md) · [Nächstes Kapitel](14_comprehensions_sortieren.md)

**Stufe:** Aufbau  
**Suchbegriffe:** default mutable args kwargs scope global nonlocal positional keyword Parameter

## Wozu brauche ich das?

Funktionen können Pflichtwerte und optionale Werte annehmen. Ein Gültigkeitsbereich beschreibt, an welcher Stelle ein Name verfügbar ist. Lokale Variablen einer Funktion sollen möglichst nicht von außen verändert werden müssen.

## Erst verstehen

**Standardargumente** greifen, wenn beim Aufruf kein Wert angegeben wird. `*args` sammelt zusätzliche positionale Argumente als Tupel, `**kwargs` zusätzliche benannte Argumente als Dictionary. Die Namen args und kwargs sind Konventionen; die Sterne bewirken das Verhalten.

## Fall 1: Pflichtwerte und benannte Optionen

Eine Begrüßung braucht einen Namen, aber nur manchmal einen besonderen Gruß.

```python
def greet(name, *, greeting="Hallo"):
    return f"{greeting} {name}"

print(greet("Basti"))
print(greet("Ada", greeting="Guten Morgen"))
```

**Erwartete Ausgabe:**

```text
Hallo Basti
Guten Morgen Ada
```

**Schritt für Schritt:**

1. `name` ist verpflichtend.
2. `greeting` besitzt einen Standardwert.
3. Das einzelne `*` verlangt für folgende Parameter benannte Argumente. Dadurch wird ein Aufruf besser lesbar.

**Achte darauf:** Ein `/` in einer Parameterliste hat die umgekehrte Rolle: Parameter davor dürfen nur positional übergeben werden. Nutze diese Sonderformen erst, wenn sie die Schnittstelle klarer machen.

[Beispieldatei öffnen](../beispiele/13_parameter_scope/fall_01.py)

```powershell
python ./beispiele/13_parameter_scope/fall_01.py
```

## Fall 2: Veränderbare Standardwerte vermeiden

Jeder Aufruf ohne übergebene Liste soll eine neue Liste bekommen.

```python
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

print(add_tag("Python"))
print(add_tag("SQL"))
existing = ["HTML"]
print(add_tag("CSS", existing))
print(existing)
```

**Erwartete Ausgabe:**

```text
['Python']
['SQL']
['HTML', 'CSS']
['HTML', 'CSS']
```

**Schritt für Schritt:**

1. Standardargumente werden bei der Funktionsdefinition ausgewertet. `tags=[]` würde daher dieselbe Liste wiederverwenden.
2. Mit `None` als Platzhalter wird bei Bedarf im Aufruf eine neue Liste erzeugt.
3. Wird eine Liste ausdrücklich übergeben, verändert diese Funktion sie bewusst. Dieses Verhalten sollte dokumentiert sein.

[Beispieldatei öffnen](../beispiele/13_parameter_scope/fall_02.py)

```powershell
python ./beispiele/13_parameter_scope/fall_02.py
```

## Fall 3: Variable Argumentanzahl und lokale Namen

Du möchtest Werte sammeln und einen äußeren Namen unverändert lassen.

```python
def total(*numbers):
    return sum(numbers)

def describe(**details):
    return ", ".join(f"{key}={value}" for key, value in details.items())

name = "Außen"
def local_name():
    name = "Innen"
    return name

print(total(2, 3, 4))
print(describe(name="Ada", role="Developer"))
print(local_name(), name)
```

**Erwartete Ausgabe:**

```text
9
name=Ada, role=Developer
Innen Außen
```

**Schritt für Schritt:**

1. Die Sterne sammeln unterschiedlich viele Argumente. Bei einem Aufruf können `*liste` und `**dictionary` Werte wieder entpacken.
2. Die Funktion `local_name()` bindet einen eigenen lokalen Namen.
3. Der äußere Name bleibt unverändert. Übergabe und Rückgabe sind meist klarer als versteckte Änderungen mit `global` oder `nonlocal`.

[Beispieldatei öffnen](../beispiele/13_parameter_scope/fall_03.py)

```powershell
python ./beispiele/13_parameter_scope/fall_03.py
```

## Typische Stolperstellen

Eine Zuweisung innerhalb einer Funktion macht den Namen normalerweise lokal. Wenn du diesen Namen davor lesen willst, kann `UnboundLocalError` entstehen. `global` verweist auf den Modulbereich, `nonlocal` auf einen umschließenden Funktionsbereich; sie sind Spezialwerkzeuge, keine normale Ersatzlösung für Parameter.

## Selbst anwenden

[Übung 13](../90_uebungen/13_parameter_scope.md) · [Starterdatei](../90_uebungen/13_parameter_scope.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/controlflow.html#more-on-defining-functions)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
