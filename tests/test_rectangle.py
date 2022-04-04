from src.Rectangle import Rectangle
from src.Circle import Circle

rectangle = Rectangle(name='Прямоугольник', width=10, height=11)


def test_rectangle_area():
    assert rectangle.area() == 110


def test_rectangle_perimeter():
    assert rectangle.perimeter() == 42


def test_rectangle_name():
    assert rectangle.name == 'Прямоугольник'


def test_rectangle_add_area():
    circle = Circle(radius=10, name='Круг')

    assert rectangle.add_area(circle) == 424.16
