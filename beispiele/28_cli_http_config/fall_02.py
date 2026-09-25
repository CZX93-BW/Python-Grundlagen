"""Kommandozeile, Konfiguration und HTTP: Konfiguration ausdrücklich umwandeln."""

import os
from unittest.mock import patch

with patch.dict(os.environ, {"APP_DEBUG": "false", "APP_PORT": "8000"}):
    debug = os.getenv("APP_DEBUG", "false").strip().casefold() == "true"
    port = int(os.getenv("APP_PORT", "8000"))
    print(debug, port)
