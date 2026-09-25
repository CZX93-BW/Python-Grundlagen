"""Klassen, Objekte und Methoden: Eine berechnete Eigenschaft anbieten."""

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Seiten müssen positiv sein")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 3)
print(rectangle.area)
rectangle.width = 5
print(rectangle.area)
