"""Asynchroner Code und Laufzeit verstehen: Eine Coroutine ausführen."""

import asyncio

async def greet():
    await asyncio.sleep(0)
    return "Hallo aus async"

print(asyncio.run(greet()))
