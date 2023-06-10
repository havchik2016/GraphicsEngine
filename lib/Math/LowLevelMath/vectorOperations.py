import lib.Math.LowLevelMath.matrixOperations as mtx
import lib.Exceptions.MathExceptions.mathExceptions as mathex


class Vector(mtx.Matrix):
    def __init__(self, item):
        if isinstance(item, int):
            super().__init__(1, item)
        elif isinstance(item, list):
            if len(item) == 1 and isinstance(item[0], list):
                super().__init__([[num] for num in item[0]])
            else:
                super().__init__([item])
        else:
            raise mathex.VectorException("Illegal argument types!")

    def scalar_product(self, v2: "Vector") -> float:
        if isinstance(v2, Vector):
            if self.dim() == v2.dim():
                return sum(self[i] * v2[i] for i in range(self.dim()))
            else:
                raise mathex.VectorException("Vector dimensions need to be the same!")
        else:
            raise mathex.VectorException("Scalar product can only be implemented between two vectors!")

    def __mod__(self, other: "Vector") -> float:
        return self.scalar_product(other)

    def __xor__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise mathex.VectorException("Orthogonal product can only be implemented with two vectors!")
        if self.dim() != other.dim() or self.dim() != 3:
            raise mathex.VectorException("Both vectors must be 3-dimensional!")
        res = Vector(3)
        res[0] = self[1] * other[2] - self[2] * other[1]
        res[1] = -(self[0] * other[2] - self[2] * other[0])
        res[2] = self[0] * other[1] - self[1] * other[0]
        return res

    def vector_product(self, other):
        return self ^ other

    def __pow__(self, other: "Vector") -> "Vector":
        return self ^ other

    def length(self) -> float:
        return self.norm()

    def normalize(self) -> "Vector":
        return self / self.length()

    def dim(self) -> int:
        if len(self.elements[0]) == 1:
            return self.n
        else:
            return self.m

    def __getitem__(self, index: int) -> float:
        if not isinstance(index, int) or not 0 <= index < self.dim():
            raise mathex.VectorException("Index is out of bounds!")
        if self.is_vertical():
            return self.elements[index][0]
        else:
            return self.elements[0][index]

    def __setitem__(self, key: int, value: float):
        if not isinstance(key, int) or not 0 <= key < self.dim():
            raise mathex.VectorException("Index is out of bounds!")
        if not isinstance(value, (int, float)):
            raise mathex.VectorException("Value can be an integer or a real number!")
        if self.is_vertical():
            self.elements[key][0] = value
        else:
            self.elements[0][key] = value

    def is_vertical(self):
        return self.n == self.dim()

    def is_horizontal(self):
        return self.m == self.dim()


def bilinear_form(m: mtx.Matrix, v1: Vector, v2: Vector) -> float:
    if not isinstance(m, mtx.Matrix) or not isinstance(v1, Vector) or \
            not isinstance(v2, Vector):
        raise mathex.VectorException("Illegal argument types!")
    if v1.dim() != m.size()[0] or m.size()[1] != v2.dim() or v1.dim() != v2.dim():
        raise mathex.VectorException("Wrong matrix / vector sizes!")
    used1 = v1 if v1.is_horizontal() else v1.transpose()
    used2 = v2 if v2.is_vertical() else v2.transpose()
    return (used1 * m * used2)[0][0]


class VectorSpace:
    def __init__(self, item):
        if not isinstance(item, list):
            raise mathex.VectorSpaceInitException("Illegal argument type!")
        if not all(isinstance(x, Vector) for x in item):
            raise mathex.VectorSpaceInitException("All elements must be vectors!")
        n = len(item)
        if n == 0:
            raise mathex.VectorSpaceInitException("List must be nonempty!")
        if not all(x.dim() == n for x in item):
            raise mathex.VectorSpaceInitException("All vectors must have the same size as their amount!")
        m = mtx.Matrix(n, n)
        for i in range(n):
            for j in range(n):
                m[i, j] = item[i][j]
        self.basis = item
        for i in range(n):
            if self.basis[i].is_vertical():
                self.basis[i] = Vector(self.basis[i].transpose().elements[0])
        if m.determinant() == 0:
            raise mathex.VectorSpaceInitException("Vectors must be independent!")

    def scalar_product(self, v1: Vector, v2: Vector) -> float:
        return bilinear_form(mtx.Matrix.gram(*self.basis), v1, v2)

    def vector_product(self, v1: Vector, v2: Vector) -> Vector:
        if not isinstance(v1, Vector) or not isinstance(v2, Vector):
            raise mathex.VectorSpaceOperationException("Both inputs must be vectors!")
        if len(self.basis) != 3 or v1.dim() != 3 or v2.dim() != 3:
            raise mathex.VectorSpaceOperationException("Need to have both vectors be 3-dimensional and basis, too!")
        res = Vector(3)
        res += self.basis[1].vector_product(self.basis[2]) * (v1[1] * v2[2] - v1[2] * v2[1])
        res += self.basis[2].vector_product(self.basis[0]) * (v1[0] * v2[2] - v1[2] * v2[0])
        res += self.basis[0].vector_product(self.basis[1]) * (v1[0] * v2[1] - v1[1] * v2[0])
        return res

    def as_vector(self, pt: "Point") -> Vector:
        m = mtx.Matrix([elem.elements[0] for elem in self.basis])
        m = m.transpose()
        v = Vector(pt.elements)
        res = m.inverse() * v
        return res.transpose()


class Point(Vector):
    def __init__(self, item):
        if isinstance(item, Vector):
            super().__init__([item[i] for i in range(item.dim())])
        super().__init__(item)

    def __add__(self, other: Vector) -> "Point":
        if not isinstance(other, Vector):
            raise mathex.PointException("Point can only be added with a vector!")
        if self.dim() != other.dim():
            raise mathex.PointException("Point and vector must have the same number of dimensions!")
        res = Point(self.dim())
        for i in range(self.dim()):
            res[i] = self[i] + other[i]
        return res

    def __iadd__(self, other: Vector):
        res = self + other
        for i in range(self.dim()):
            self[i] = res[i]

    def __sub__(self, other: Vector) -> "Point":
        if not isinstance(other, Vector):
            raise mathex.PointException("Point can only be added with a vector!")
        if self.dim() != other.dim():
            raise mathex.PointException("Point and vector must have the same number of dimensions!")
        res = Point(self.dim())
        for i in range(self.dim()):
            res[i] = self[i] - other[i]
        return res

    def __isub__(self, other: Vector):
        res = self - other
        for i in range(self.dim()):
            self[i] = res[i]

    def __mul__(self, other):
        raise mathex.PointException("Illegal operation")

    def __rmul__(self, other):
        raise mathex.PointException("Illegal operation")

    def __imul__(self, other):
        raise mathex.PointException("Illegal operation")

    def __truediv__(self, other):
        raise mathex.PointException("Illegal operation")

    def __invert__(self):
        raise mathex.PointException("Illegal operation")


class CoordinateSystem:
    def __init__(self, initial: Point, basis: VectorSpace):
        self.initial_point = initial
        self.space = basis
