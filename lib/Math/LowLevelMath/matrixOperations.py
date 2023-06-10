from lib.Exceptions.MathExceptions import mathExceptions as mathex
from copy import deepcopy
from math import sqrt, sin, cos


class Matrix:
    def __init__(self, first, second = None):
        if isinstance(first, int) and second is None:
            if first <= 0:
                raise mathex.MatrixInitException("Matrix size must be nonnegative!")
            self.n = first
            self.m = first
            self.elements = [[0 for _ in range(self.n)] for _ in range(self.n)]
        elif isinstance(first, int) and isinstance(second, int):
            if first <= 0 or second <= 0:
                raise mathex.MatrixInitException("Matrix size must be nonnegative!")
            self.n = first
            self.m = second
            self.elements = [[0 for _ in range(self.m)] for _ in range(self.n)]
        elif isinstance(first, list) and second is None:
            if len(first) == 0:
                raise mathex.MatrixInitException("Matrix must be nonempty!")
            first_len = len(first[0])
            for row in first:
                if len(row) != first_len:
                    raise mathex.MatrixInitException("All rows' lengths must be equal!")
                if not all(isinstance(item, (int, float)) for item in row):
                    raise mathex.MatrixInitException("All items must be numbers!")
            self.n = len(first)
            self.m = first_len
            self.elements = first
        else:
            raise mathex.MatrixInitException("Illegal argument types!")

    def __eq__(self, other: "Matrix") -> bool:
        return self.n == other.n and self.m == other.m and \
               self.elements == other.elements

    def __ne__(self, other: "Matrix") -> bool:
        return not self.__eq__(other)

    def addition(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise mathex.MatrixOperationException("Matrix must be added to a matrix!")
        if not self.n == other.n or not self.m == other.m:
            raise mathex.MatrixOperationException("Matrices must have the same sizes!")
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        return res

    def __add__(self, other: "Matrix") -> "Matrix":
        return self.addition(other)

    def __iadd__(self, other: "Matrix"):
        self.elements = self.__add__(other).elements

    def __sub__(self, other: "Matrix") -> "Matrix":
        return self.addition(-1 * other)

    def __isub__(self, other: "Matrix"):
        self.elements = self.__sub__(other).elements

    def multiplication(self, other):
        if isinstance(other, Matrix):
            if self.m != other.n:
                raise mathex.MatrixOperationException("Illegal matrix sizes!")
            res = Matrix(self.n, other.m)
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        res.elements[i][j] += self.elements[i][k] * other.elements[k][j]
            return res
        elif isinstance(other, (int, float)):
            res = Matrix(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    res.elements[i][j] = other * self.elements[i][j]
            return res
        else:
            raise mathex.MatrixOperationException("Wrong argument type!")

    def __mul__(self, other) -> "Matrix":
        return self.multiplication(other)

    def __rmul__(self, other) -> "Matrix":
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, Matrix):
            res = self.multiplication(other)
            self.m = other.m
            self.elements = res.elements
        else:
            self.elements = self.multiplication(other).elements

    def get_minor(self, rows: list[int], cols: list[int]) -> "Matrix":
        if not isinstance(rows, list) or not isinstance(cols, list):
            raise mathex.MatrixOperationException("You must a list of lines to exclude!")
        if not all(isinstance(item, int) for item in rows) or \
                not all(isinstance(item, int) for item in cols):
            raise mathex.MatrixOperationException("All values must be integers!")
        if not all(0 <= item <= self.n - 1 for item in rows) or \
                not all(0 <= item <= self.m - 1 for item in cols):
            raise mathex.MatrixOperationException("All values must be inbounds!")
        if len(set(rows)) != len(rows) or len(set(cols)) != len(cols):
            raise mathex.MatrixOperationException("All rows and cols must be unique!")
        n1 = len(rows)
        m1 = len(cols)
        res = Matrix(self.n - n1, self.m - m1)
        rows_set = set(rows)
        cols_set = set(cols)
        r1 = 0
        for i in range(self.n):
            if i in rows_set:
                r1 += 1
                continue
            c1 = 0
            for j in range(self.m):
                if j in cols_set:
                    c1 += 1
                    continue
                res.elements[i - r1][j - c1] = self.elements[i][j]
        return res

    def determinant(self) -> float:
        if self.n != self.m:
            raise mathex.MatrixOperationException("Determinant can only be computed for square matrices!")
        sign = 1
        mat_copy = Matrix(deepcopy(self.elements))
        for i in range(self.n):
            if mat_copy.elements[i][i] == 0:
                found_nonzero = False
                for j in range(i + 1, self.n):
                    if mat_copy.elements[j][i] != 0:
                        found_nonzero = True
                        sign *= -1
                        for k in range(i, self.n):
                            mat_copy.elements[i][k], mat_copy.elements[j][k] = \
                                mat_copy.elements[j][k], mat_copy.elements[i][k]
                        break
                if not found_nonzero:
                    return 0
            for j in range(i + 1, self.n):
                mult = -mat_copy.elements[j][i] / mat_copy.elements[i][i]
                for k in range(i, self.n):
                    mat_copy.elements[j][k] += mult * mat_copy.elements[i][k]
        prod = sign
        for i in range(self.n):
            prod *= mat_copy.elements[i][i]
        return prod

    def inverse(self) -> "Matrix":
        if self.n != self.m:
            raise mathex.MatrixOperationException("Only square matrices can be inverted!")
        if self.determinant() == 0:
            raise mathex.MatrixOperationException("Only matrices with nonzero determinant are invertible!")
        det = self.determinant()
        res = Matrix(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                minor = self.get_minor([i], [j])
                adjoint = ((-1) ** (i + j)) * minor.determinant()
                res.elements[j][i] = adjoint / det
        return res

    def transpose(self) -> "Matrix":
        res = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                res.elements[i][j] = self.elements[j][i]
        return res

    def __truediv__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            return self * other.inverse()
        elif isinstance(other, (int, float)):
            if other == 0:
                raise mathex.MatrixOperationException("Can't divide by zero!")
            return self * (1 / other)
        else:
            raise mathex.MatrixOperationException("Illegal argument types!")

    def norm(self) -> float:
        s = 0
        for i in range(self.n):
            for j in range(self.m):
                s += self.elements[i][j] ** 2
        return sqrt(s)

    def __invert__(self) -> "Matrix":
        return self.inverse()

    @staticmethod
    def identity(n: int) -> "Matrix":
        m = Matrix(n)
        for i in range(n):
            m.elements[i][i] = 1
        return m

    def __getitem__(self, item):
        if isinstance(item, tuple):
            if len(item) != 2:
                raise mathex.MatrixOperationException("Matrix has 2 dimensions!")
            if not (0 <= item[0] < self.n) or not (0 <= item[1] < self.m):
                raise mathex.MatrixOperationException("Indices are out of bounds!")
            return self.elements[item[0]][item[1]]
        elif isinstance(item, int):
            return self.elements[item]
        else:
            raise mathex.MatrixOperationException("Illegal argument type!")

    def __setitem__(self, key, item: float):
        if isinstance(key, tuple):
            if len(key) != 2:
                raise mathex.MatrixOperationException("Matrix has 2 dimensions!")
            if not (0 <= key[0] < self.n) or not (0 <= key[1] < self.m):
                raise mathex.MatrixOperationException("Indices are out of bounds!")
            self.elements[key[0]][key[1]] = item
        else:
            raise mathex.MatrixOperationException("Illegal argument type!")

    def size(self) -> tuple:
        return self.n, self.m

    @staticmethod
    def gram(*args) -> "Matrix":
        if len(args) == 0:
            raise mathex.MatrixOperationException("There must be at least one vector!")
        c = 0
        for x in args:
            c += 1
        if not all(arg.dim() == c for arg in args):
            raise mathex.VectorException("All vectors must have the same dimensions as their amount!")
        res = Matrix(c, c)
        i = 0
        for x in args:
            j = 0
            for y in args:
                res[i][j] = x.scalar_product(y)
                j += 1
            i += 1
        return res

    @staticmethod
    def get_rotation_matrix(inds: (int, int), angle: float, n: int) -> "Matrix":
        if not isinstance(inds, tuple) or not isinstance(angle, float) or not isinstance(n, int):
            raise mathex.MatrixOperationException("Illegal argument types!")
        if len(inds) != 2 or not isinstance(inds[0], int) or not isinstance(inds[1], int):
            raise mathex.MatrixOperationException("Indices must be 2 integers!")
        i, j = inds
        if not (0 <= i < n) or not (0 <= j < n):
            raise mathex.MatrixOperationException("Indices are out of bounds!")
        res = Matrix.identity(n)
        res[i, i] = cos(angle)
        res[j, j] = cos(angle)
        res[i, j] = ((-1) ** (i + j)) * sin(angle)
        res[j, i] = ((-1) ** (i + j + 1)) * sin(angle)
        return res

    @staticmethod
    def get_teit_bryan_matrix(angles: (float, float, float)) -> "Matrix":
        if not isinstance(angles, tuple) or len(angles) != 3:
            raise mathex.MatrixOperationException("Angles must be a length 3 tuple!")
        if not all(isinstance(num, float) for num in angles):
            raise mathex.MatrixOperationException("All angles must be floats!")
        m3 = Matrix.get_rotation_matrix((0, 1), angles[2], 3)
        m2 = Matrix.get_rotation_matrix((0, 2), angles[1], 3)
        m1 = Matrix.get_rotation_matrix((1, 2), angles[0], 3)
        return m1 * m2 * m3
