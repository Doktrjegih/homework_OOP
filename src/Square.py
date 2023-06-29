from src.Figure import Figure


class Square(Figure):
    def __init__(self, side, name):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4
