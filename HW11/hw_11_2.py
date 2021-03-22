class CheckNull(Exception):
    def __init__(self, txt):
        self.txt = txt


first = input("Введите число: ")
second = input("Введите число <>0: ")

try:
    first = int(first)
    second = int(second)
    if second == 0:
        raise CheckNull("Вы ввели 0")
except ValueError:
    print("Вы ввели не число")
except CheckNull as err:
    print(err)
else:
    print(f"Результат: {first / second}")
