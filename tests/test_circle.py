from src.Square import Square
from src.Circle import Circle


def test_circle_area():
    circle = Circle(name='Круг', radius=10)
    assert round(circle.area(), 2) == 314.16


def test_circle_perimeter():
    circle = Circle(name='Круг', radius=10)
    assert round(circle.perimeter(), 2) == 62.83


def test_circle_name():
    circle = Circle(name='Круг', radius=10)
    assert circle.name == 'Круг'


def test_circle_add_area():
    circle = Circle(name='Круг', radius=10)
    square = Square(side=10, name='Квадрат')

    assert square.add_area(circle) == 414.16
