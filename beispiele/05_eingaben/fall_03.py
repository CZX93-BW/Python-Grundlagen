"""Eingaben lesen und prüfen: Bis zur gültigen Eingabe nachfragen."""

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
