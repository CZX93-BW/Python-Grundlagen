"""Kommandozeile, Konfiguration und HTTP: Eine JSON-Antwort mit prüfbarer Grenze laden."""

import json
from urllib.request import urlopen
from io import BytesIO

def fetch_title(url, opener=urlopen):
    with opener(url, timeout=5) as response:
        data = json.load(response)
    if not isinstance(data, dict) or not isinstance(data.get("title"), str):
        raise ValueError("Antwort braucht einen Text in title")
    return data["title"]

def fake_open(url, *, timeout):
    return BytesIO(b'{"title": "Python lernen"}')

print(fetch_title("https://example.invalid/note", opener=fake_open))
