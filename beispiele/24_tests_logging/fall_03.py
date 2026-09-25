"""Tests, Fehlersuche und Logging: Einen Fehler eingrenzen."""

def price_per_item(total, quantity):
    if quantity <= 0:
        raise ValueError("quantity muss positiv sein")
    return total / quantity

for quantity in [2, 0]:
    try:
        print(price_per_item(10, quantity))
    except ValueError as error:
        print(f"Eingabe quantity={quantity}: {error}")
