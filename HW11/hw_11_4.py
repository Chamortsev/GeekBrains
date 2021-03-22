class WMS:

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        self.all_append = []
        self.appended = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.qty}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.qty}'

    def arrival(self):
        while True:
            try:
                unit_name = input(f'Введите Название Бренда: ')
                unit_price = int(input(f'Введите цену за шт: '))
                unit_qty = int(input(f'Введите количество: '))
                unique = {'Модель устройства': unit_name, 'Цена за ед': unit_price, 'Количество': unit_qty}
                self.my_unit.update(unique)
                self.all_append.append(self.my_unit)
                print(f'Текущий список -\n {unique}')
                insert = input(f'Хотите продолжить? Y/N').lower()
                if insert == 'n':
                    print('До новых встреч')
                    return f'{self.all_append}'
                    break
            except:
                return f'Ошибка ввода данных'


class Printer(WMS):
    def to_print(self):
        return f'Просто вывод названия {self.name}'


class Scanner(WMS):
    def to_scan(self):
        return f'Просто вывод названия {self.name}'


class Xerox(WMS):
    def to_copier(self):
        return f'Просто вывод названия {self.name}'


p = Printer('hp', 2000, 5)
s = Scanner('Canon', 1200, 5)
x = Xerox('Xerox', 1500, 1)
print(p.arrival())
print(s.arrival())
print(x.arrival())
print(p.to_print())
print(x.to_copier())
