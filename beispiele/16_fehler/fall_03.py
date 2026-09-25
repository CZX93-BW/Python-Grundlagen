"""Fehler verstehen und gezielt behandeln: Eigene Fehler mit Ursache."""

class ConfigurationError(Exception):
    """Signal invalid application configuration."""

def read_port(raw_value):
    try:
        return int(raw_value)
    except ValueError as error:
        raise ConfigurationError("Port muss eine ganze Zahl sein") from error

try:
    read_port("abc")
except ConfigurationError as error:
    print(error)
    print(type(error.__cause__).__name__)
