tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Инокентий', 'Иванан'
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


check(tutors, klasses)
print(*zip(tutors, klasses))
