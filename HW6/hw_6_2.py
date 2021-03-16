unic = set()
full = []
max_income = 0
with open('nginx_logs.txt', 'r') as f:
    line = f.readline()
    while line:
        content = line.split()
        unic.add(content[0])
        full.append(content[0])
        line = f.readline()

for i in unic:
    my_count = full.count(i)
    if my_count > max_income:
        max_income = my_count
        spam = i
print('IP спамера: ', spam, "Количество вхождений:", max_income)
