"""Tests, Fehlersuche und Logging: Ereignisse protokollieren."""

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)
logger.debug("Detail nur bei DEBUG")
logger.info("Verarbeitung gestartet")
logger.warning("Ein Datensatz wurde übersprungen")
