"""Asynchroner Code und Laufzeit verstehen: Messen, bevor du optimierst."""

from time import perf_counter

start = perf_counter()
result = sum(range(100_000))
elapsed = perf_counter() - start
print(result)
print(elapsed >= 0)
