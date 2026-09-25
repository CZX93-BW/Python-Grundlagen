"""Asynchroner Code und Laufzeit verstehen: Mehrere wartende Abläufe starten."""

import asyncio

async def load(label):
    await asyncio.sleep(0.01)
    return label.upper()

async def main():
    results = await asyncio.gather(load("eins"), load("zwei"))
    print(results)

asyncio.run(main())
