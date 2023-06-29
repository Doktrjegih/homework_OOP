from src.Triangle import Triangle
from src.Square import Square
from src import Wrong

triangle = Triangle(name='Треугольник', side1=10, side2=11, side3=12)


def test_triangle_area():
    assert round(triangle.area(), 2) == 51.52


def test_triangle_perimeter():
    assert triangle.perimeter() == 33


def test_triangle_name():
    assert triangle.name == 'Треугольник'


def test_triangle_add_area():
    square = Square(side=10, name='Квадрат')
    assert triangle.add_area(square) == 151.52


# далее общие проверки, для которых решил не создавать отдельный файл

def test_impossible_triangle():
    Triangle(name='Треугольник', side1=10, side2=0, side3=12)


def test_wrong_class():
    square = Wrong.WrongClass()
    assert triangle.add_area(square)


def test_added_class_without_method():
    square = Wrong.ClassWithoutMethod(name='Класс без метода "area"')
    assert triangle.add_area(square)


def test_main_class_without_method():
    triangle = Wrong.ClassWithoutMethod(name='Класс без метода "area"')
    square = Square(side=10, name='Квадрат')
    assert triangle.add_area(square)
