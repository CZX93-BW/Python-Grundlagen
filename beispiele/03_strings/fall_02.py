"""Texte bearbeiten und formatieren: Aufteilen, verbinden und ersetzen."""

text = "Apfel,Birne,Kiwi"
fruits = text.split(",")
print(fruits)
print(" | ".join(fruits))
print(text.replace("Kiwi", "Mango"))
print(text.startswith("Apfel"))
