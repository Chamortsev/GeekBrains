import sys
file = 'bakery.csv'

str_number = sys.argv[1]

with open(file, 'a') as f:
    f.write('\n' + str(str_number))
