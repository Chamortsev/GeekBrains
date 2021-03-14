def logger(func):
    def wrapper(*args):
        result = type(*args)
        return f'{func.__name__}({args}:{result})'

    return wrapper


@logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)

print(a)
