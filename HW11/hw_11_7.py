class ComplexNumber:
    def __init__(self, a_input, b_input):
        self.a = a_input
        self.b = b_input
        self.z = a_input * b_input

    def __add__(self, other):
        return f'Self sum A+B = {self.a + self.b} '
        return f'Other sum A+B = {other.a + other.b} '

    def __mul__(self, other):
        return f'Self A*B - other A*B = {(self.a * self.a) - (other.a * other.b)} '

    def __str__(self):
        return f'Str  = {self.a} + {self.b}'


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
print(a)
print(a + b)
print(a * b)
