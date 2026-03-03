import math


def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2

print("Процедурний підхід:")
print("Прямокутник (5, 10):", rectangle_area(5, 10))
print("Коло (7):", circle_area(7))


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

print("\nООП підхід:")
rect = Rectangle(5, 10)
circ = Circle(7)
print("Прямокутник (5, 10):", rect.area())
print("Коло (7):", circ.area())