class Cell:
    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        return f'Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.{self.param + other.param}'

    def __sub__(self, other):
        check = self.param - other.param
        return f'Вычитание. Участвуют две клетки.{check}' if check > 0 else f'Разность количества клеток меньше или = 0'

    def __mul__(self, other):
        return f'Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток. {self.param * other.param}'

    def __floordiv__(self, other):
        return f'Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток. {self.param // other.param}'

    def __truediv__(self, other):
        return f'Деление. Создаётся общая клетка из двух. Простое деление {int(self.param / other.param)}'

    def make_order(self, rows):
        result = ''
        for i in range(self.param // rows):
            result = result + '*' * rows + '\n'
        result = result + '*' * (self.param % rows) + '\n'
        return result


cell_a = Cell(10)
cell_b = Cell(10)
print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_a * cell_b)
print(cell_a // cell_b)

print(cell_a / cell_b)
print(cell_a.make_order(3))
