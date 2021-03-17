class Car:

    def __init__(self, speed, color, name, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        return f'Автомобиль {self.name} поехал.'

    def stop(self):
        return f'Автомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул на {direction}'

    def show_speed(self):
        return f'Скорость автомобиля {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            up_speed = self.speed - 60
            return f'Ваша скорость {self.speed}. Вы привысили скорость на {up_speed} км.'
        else:
            return ''


class SportCar(Car):
    def show_speed(self):
        if self.speed > 80:
            up_speed = self.speed - 80
            return f'Ваша скорость {self.speed}. Вы привысили скорость на {up_speed} км. Лучше переместиться на спортивную трассу'
        else:
            return ''


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            up_speed = self.speed - 40
            return f'Ваша скорость {self.speed}. Вы привысили скорость на {up_speed} км.'
        else:
            return ''


class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 70:
            return f'Скорость {self.speed}. Нужно включить люстру, скорость больше положенной.'
        else:
            return ''


car = TownCar(60, 'красный', 'WW', False)
print(car.go(), car.show_speed(), car.turn('направо'), car.stop())

car = TownCar(70, 'белый', 'Ford', False)
print(car.go(), car.show_speed(), car.turn('прямо'), car.stop())

car = SportCar(70, 'черный', 'Lamborgini', False)
print(car.go(), car.show_speed(), car.turn('прямо'), car.stop())

car = PoliceCar(70, 'красный', 'Ferrary', True)
print(car.go(), car.show_speed(), car.turn('налево'), car.stop())
