"""Zählen, gruppieren und Muster erkennen: Häufigkeiten zählen und Daten gruppieren."""

from collections import Counter, defaultdict

counts = Counter(["Apfel", "Birne", "Apfel"])
print(counts["Apfel"], counts["Kiwi"])
groups = defaultdict(list)
for name in ["Ada", "Anna", "Basti"]:
    groups[name[0]].append(name)
print(dict(groups))
