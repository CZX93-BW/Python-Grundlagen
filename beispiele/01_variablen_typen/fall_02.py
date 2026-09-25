"""Variablen und Datentypen: Werte ändern und umwandeln."""

quantity_text = "3"
quantity = int(quantity_text)
quantity += 2
print(quantity)
print(str(quantity) + " Artikel")
print(isinstance(quantity, int))
