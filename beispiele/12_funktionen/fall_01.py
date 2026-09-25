"""Funktionen und Rückgabewerte: Eine Berechnung wiederverwenden."""

def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height

area = rectangle_area(4, 3)
print(area)
print(rectangle_area(height=5, width=2))
