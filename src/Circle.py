from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * 2 * self.radius
