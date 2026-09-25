"""Parameter, Standardwerte und Gültigkeitsbereiche: Veränderbare Standardwerte vermeiden."""

def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

print(add_tag("Python"))
print(add_tag("SQL"))
existing = ["HTML"]
print(add_tag("CSS", existing))
print(existing)
