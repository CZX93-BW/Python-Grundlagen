"""Musterlösung 29: Eine Coroutine schreiben."""

import asyncio

async def async_double(number: int) -> int:
    """Yield control once, then return twice the input."""
    await asyncio.sleep(0)
    return number * 2
