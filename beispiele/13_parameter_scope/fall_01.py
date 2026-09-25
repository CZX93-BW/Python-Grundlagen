"""Parameter, Standardwerte und Gültigkeitsbereiche: Pflichtwerte und benannte Optionen."""

def greet(name, *, greeting="Hallo"):
    return f"{greeting} {name}"

print(greet("Basti"))
print(greet("Ada", greeting="Guten Morgen"))
