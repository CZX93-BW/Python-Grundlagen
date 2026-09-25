"""Entscheidungen mit if und match: Feste Befehle mit match behandeln."""

command = "list"
match command:
    case "list" | "show":
        print("Einträge anzeigen")
    case "quit":
        print("Beenden")
    case _:
        print("Unbekannter Befehl")
