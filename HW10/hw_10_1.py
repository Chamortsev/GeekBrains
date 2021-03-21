class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in self.matrix:
            print(f'{i}')

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for k in range(len(other.matrix[i])):
                self.matrix[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix.__str__(self)


m = Matrix(([31, 22], [37, 43], [51, 86]))
m.__str__()
print('')
m = Matrix(([3, 5, 32], [2, 4, 6], [-1, 64, -8]))
m.__str__()
print('')
m = Matrix(([3, 5, 8, 3], [8, 3, 7, 1]))
m.__str__()
print('')
m1 = Matrix(([3, 5, 32], [2, 4, 6]))
m2 = Matrix(([3, 5, 8], [8, 3, 7]))

print(m1.__add__(m2))
