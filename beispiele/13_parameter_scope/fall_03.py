"""Parameter, Standardwerte und Gültigkeitsbereiche: Variable Argumentanzahl und lokale Namen."""

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
