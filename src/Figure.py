class Figure:
    def __init__(self, name):
        self.name = name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Передан неправильный класс')
        if not hasattr(self, 'area'):
            raise AttributeError(f'Для главного объекта {self} отсутствует метод "area"')
        if not hasattr(figure, 'area'):
            raise AttributeError(f'Для добавляемого объекта {figure} отсутствует метод "area"')
        return round(self.area(), 2) + round(figure.area(), 2)
