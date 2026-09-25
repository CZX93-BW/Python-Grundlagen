"""Kommandozeile, Konfiguration und HTTP: Argumente mit argparse lesen."""

import argparse

parser = argparse.ArgumentParser(description="Eine Begrüßung ausgeben")
parser.add_argument("name")
parser.add_argument("--count", type=int, default=1)
args = parser.parse_args(["Basti", "--count", "2"])
for _ in range(args.count):
    print(f"Hallo {args.name}")
