"""Fehler verstehen und gezielt behandeln: Genau den erwarteten Fehler fangen."""

for raw_value in ["12", "abc"]:
    try:
        number = int(raw_value)
    except ValueError as error:
        print(f"Ungültige Zahl: {raw_value}")
    else:
        print(number * 2)
    finally:
        print("Versuch abgeschlossen")
