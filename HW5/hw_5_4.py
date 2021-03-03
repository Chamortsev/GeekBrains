src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Вариант решения 1
tmp =src[0]
result = []
for i in src:
        if (i) > tmp:
             tmp=(i)
             result.append(i)
        tmp=(i)
print(result)

# Вариант решения 2
tmp =src[0]

unique_gen = set()
temp =set()
for i in src:
    if (i) > tmp:
        unique_gen.add(i)
    else:
        unique_gen.discard(i)
    temp.add(i)
    tmp = (i)
print(unique_gen)




