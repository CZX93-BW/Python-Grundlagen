"""Tupel, Sets und die passende Sammlung: Ein Set verändern."""

processed_ids = set()
processed_ids.add(3)
processed_ids.add(3)
processed_ids.update([4, 5])
processed_ids.discard(99)
processed_ids.remove(4)
print(sorted(processed_ids))
print(3 in processed_ids)
