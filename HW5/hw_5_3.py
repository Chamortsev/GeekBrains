tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Инокентий', 'Иванан'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

matrix_zip = [
    (row_1, row_2) for row_1, row_2 in zip(tutors, klasses)
]


def check(a, b):
    if len(a) > len(b):
        c = len(a) - len(b)
        for i in range(c):
            klasses.append(None)
    print(*zip(tutors, klasses))


check(tutors, klasses)

# -----Второй вариант подсказанный коллегами по цеху с испльзованием zip_longest

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Инокентий', 'Иванан']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

wd_new = [result for row in zip_longest(tutors, klasses, fillvalue=None) for result in row]
print(wd_new)
