import pytest
from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle


@pytest.fixture(scope='module')
def create_circle():
    return Circle(name='Круг', radius=10)


@pytest.fixture(scope='module')
def create_square():
    return Square(name='Квадрат', side=10)


@pytest.fixture(scope='module')
def create_triangle():
    return Triangle(name='Треугольник', side_1=13, side_2=14, side_3=15)


@pytest.fixture(scope='module')
def create_rectangle():
    return Rectangle(name='Прямоугольник', height=10, width=11)
