class Matrix:

    def __init__(self, ll):
        self.matrix = ll

    def __repr__(self):
        return '\n'.join(' '.join(str(val) for val in row) for row in self.matrix)

    def vals(self):
        return self.matrix

    def dims(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.dims() != other.dims():
            raise ValueError("Sečítat lze pouze matice stejných rozměrů")
        result = []
        for i, row in enumerate(self.matrix):
            result.append([x + y for x, y in zip(row, other.matrix[i])])
        return Matrix(result)

    def __sub__(self, other):
       if self.dims() != other.dims():
            raise ValueError("Odečítat lze pouze matice stejných rozměrů")
       result = []
       for i, row in enumerate(self.matrix):
            result.append([x - y for x, y in zip(row, other.matrix[i])])
       return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.dims()[1] != other.dims()[0]:
                raise ValueError("Násobit lze pouze matice kompatibilních rozměrů")
            result = [[0] * len(other.matrix[0]) for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        else:
            result = [[x * other for x in row] for row in self.matrix]
            return Matrix(result)

    def is_symmetric(self):
        if len(self.matrix) != len(self.matrix[0]):
            return False
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix[0])):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True


def zero_matrix(r, c):
    return Matrix([[0] * c for _ in range(r)])


def identity_matrix(n):
    return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])