import sys
file = 'bakery.csv'

if len(sys.argv) == 2:
    str_number = sys.argv[1]
elif len(sys.argv) == 3:
    str_number = sys.argv[1]
    str_end = sys.argv[2]
else:
    str_number = 1

with open(file, 'r', encoding='utf-8') as f:
    line = f.readline()
    if len(sys.argv) < 3:
        str_end = len(line)
    for i in range(int(str_end)):
        sale = line.strip()
        if i >= int(str_number) - 1:
            print(sale)
        line = f.readline()
