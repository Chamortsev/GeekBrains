fio_key = []
hobby_key = []

with open('users.csv', 'r') as f:
    line = f.readline()
    while line:
        fio = line.strip().replace(',', ' ')
        fio_key.append(fio)
        line = f.readline()

with open('hobby.csv', 'r') as f:
    line = f.readline()
    while line:
        hobby = line.strip()
        hobby_key.append(hobby)
        line = f.readline()

if len(hobby_key) < len(fio_key):
    for i in range(len(fio_key) - len(hobby_key)):
        hobby_key.append(None)
    my_dic = dict(zip(fio_key, hobby_key))
elif len(hobby_key) == len(fio_key):
    my_dic = dict(zip(fio_key, hobby_key))
else:
    exit(code=1)

with open('my_dict.csv', 'w') as f:
    f.write(str(my_dic))
