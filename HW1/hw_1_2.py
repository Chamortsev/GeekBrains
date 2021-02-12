a = 1000
numbers = []

# Определяем чет не чет через арифмет. операцию с преобразованием в int а так использовал бы %
# Записываем в список

for i in range(a):
    z = i / 2
    if (int(z) * 2 != i):
        numbers.append(i)

print('Cумма цифр которых делится нацело на 7')
for key, number in enumerate(numbers):
    q = number ** 3 # Умножаем
    w = len(str(q))
    temp = 0
    for i in range(w):
        z = str(q)[i]
        temp = temp + int(z)
    if temp % 7 == 0:
        print(number)

print('Прибавили 17 и проверили делится ли на 7 ')
for key, number in enumerate(numbers):
    q = number + 17 ** 3  # Умножаем
    w = len(str(q))
    temp = 0
    for i in range(w):
        z = str(q)[i]
        temp = temp + int(z)
    if temp % 7 == 0:
        print(number)
