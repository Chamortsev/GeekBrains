def logger(info=0):
    def _logger(func):
        def wrapper(*args):
            result = func(*args)
            msg = f'{result}'
            if info == 1:
                if int(*args) < 0:
                    msg = f' {args}меньше 0, Выберите значение больше нуля'
                    raise ValueError(msg)
                else:
                    msg = f'{result}'
            if info > 1:
                msg = f'{func.__name__} -> {type(*args)}->{result}'
            return msg

        return wrapper

    return _logger


@logger(info=2)
def calc_cube(x):
    return x ** 3


username_f = calc_cube(-3)
print(username_f)
