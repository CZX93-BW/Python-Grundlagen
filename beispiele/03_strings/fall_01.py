"""Texte bearbeiten und formatieren: Eingaben säubern und vergleichen."""

raw_name = "  Straße  "
clean_name = raw_name.strip()
print(clean_name)
print(clean_name.casefold() == "STRASSE".casefold())
print(raw_name == clean_name)
