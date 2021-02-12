import random

# Функция приводящая к нужному формату цену
def price_norm(n):
    r = round(n)
    k = round(n % 1)
    if len(str(k)) == 1:
        k = '0' + str(k)
    else:
        k = str(k)
    return '<<' + str(r) + 'руб. ' +  k + 'коп.' + '>>'
# Создаем пустой массив
price=[]
# Заполняем массив рендомными ценами от 20.03 до 13990.0 с разрядностью 2 знака после запятой
for i in range(20):
    price.append(round(random.uniform(20.3, 13990.9), 2))
# Сортировка от меньшего к большему
price.sort()

# Вывод задания A,B
for key, i in enumerate(price):
    print(price_norm(i), end = ' ')
print('')

# Делаем копию списка цен Задание C
new_price = price.copy()
new_price = sorted(new_price, reverse = True)

# Выводим цены 5-ти самых дорогих товаров (Задание D)
for key, i in enumerate(new_price):
    print(price_norm(i), end = ' ')
print('')

for i in range(5):
    print(price_norm(new_price[i]), end = ' ')
 