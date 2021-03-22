import datetime


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def my_method_one(cls, data):
        content = data.split('-')
        y = int(content[0])
        m = int(content[1])
        d = int(content[2])
        return f'Год {y} тип {type(y)}, Месяц {m} тип {type(m)}, День {d} тип {type(d)}'

    @staticmethod
    def validate(data):
        try:
            datetime.datetime.strptime(data, '%Y-%m-%d')
            return f'Вы ввели корректную дату {data}'
        except ValueError:
            return f'Дата не в правильном формате YYYY-MM-DD или некорректна {data}'


print(Data.validate('2021-13-21'))
print(Data.validate('2021-03-21'))
print(Data.my_method_one('2021-03-21'))
