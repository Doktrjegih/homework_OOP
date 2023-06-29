from src.Figure import Figure
import math


def area_from_three_side(side1: int, side2: int, side3: int):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise AttributeError('Стороны треугольника заданы неправильно')
    half_perimeter = (side1 + side2 + side3) / 2
    p = half_perimeter
    a, b, c = side1, side2, side3
    total_area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return total_area


class Triangle(Figure):
    def __init__(self, side1, side2, side3, name):
        super().__init__(name)
        self.side1, self.side2, self.side3 = side1, side2, side3
        self.area_ = area_from_three_side(self.side1, self.side2, self.side3)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        return self.area_
