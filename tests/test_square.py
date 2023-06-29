from src.Square import Square
from src.Rectangle import Rectangle

square = Square(name='Квадрат', side=10)


def test_square_area():
    assert square.area() == 100


def test_square_perimeter():
    assert square.perimeter() == 40


def test_square_name():
    assert square.name == 'Квадрат'


def test_square_add_area():
    rectangle = Rectangle(width=5, height=7, name='Прямоугольник')

    assert square.add_area(rectangle) == 135
