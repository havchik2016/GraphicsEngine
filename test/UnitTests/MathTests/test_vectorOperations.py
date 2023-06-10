from lib.Math.LowLevelMath.matrixOperations import Matrix
import lib.Math.LowLevelMath.vectorOperations as vec
import lib.Exceptions.MathExceptions.mathExceptions as mathex
import pytest


def test_amount_init():
    v = vec.Vector(3)
    lst = [[0, 0, 0]]
    act = v.elements == lst
    assert act


def test_vertical_init():
    v = vec.Vector([[1, 2, 3]])
    lst = [[1], [2], [3]]
    act = v.elements == lst
    assert act


def test_horizontal_init():
    v = vec.Vector([4, 5, 6])
    lst = [[4, 5, 6]]
    act = v.elements == lst
    assert act


def test_illegal_init():
    with pytest.raises(mathex.MatrixInitException):
        v = vec.Vector(-1)


def test_scalar_product():
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([[4, 5, 6]])
    res = v1.scalar_product(v2)
    ans = 32
    act = res == ans
    assert act


def test_hor_dim():
    v = vec.Vector([1, 2, 3, 4])
    res = v.dim()
    ans = 4
    act = res == ans
    assert act


def test_vert_dim():
    v = vec.Vector([[1, 2, 3, 4]])
    res = v.dim()
    ans = 4
    act = res == ans
    assert act


def test_length():
    v = vec.Vector([1, 2, 2])
    res = v.length()
    ans = 3
    assert res == ans


def test_normalize():
    v = vec.Vector([1, 2, 2])
    res = v.normalize()
    ans = vec.Vector([1 / 3, 2 / 3, 2 / 3])
    act = res == ans
    assert act


def test_orthogonal_with_non_vector():
    with pytest.raises(mathex.VectorException):
        v1 = vec.Vector([1, 2, 3])
        v2 = 3
        v1 ^ v2


def test_orthogonal_with_different_dimensions():
    with pytest.raises(mathex.VectorException):
        v1 = vec.Vector([1, 2, 3])
        v2 = vec.Vector([4, 5, 6, 7])
        v1 ^ v2


def test_orthogonal_ok():
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([4, 5, 6])
    res = v1 ** v2
    ans = vec.Vector([-3, 6, -3])
    act = res == ans
    assert act


def test_wrong_type_bilinear_form():
    m = Matrix.identity(3)
    v1 = vec.Vector([1, 2, 3])
    v2 = 3
    with pytest.raises(mathex.VectorException):
        vec.bilinear_form(m, v1, v2)


def test_different_size_bilinear_form():
    m = Matrix.identity(3)
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([4, 5, 6, 7])
    with pytest.raises(mathex.VectorException):
        vec.bilinear_form(m, v1, v2)


def test_ok_bilinear_form():
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([4, 5, 6])
    m = Matrix.identity(3)
    res = vec.bilinear_form(m, v1, v2)
    ans = 32
    act = res == ans
    assert act


def test_zero_det_basis():
    v1 = vec.Vector([1, 1, 1])
    v2 = vec.Vector([1, 2, 3])
    v3 = vec.Vector([4, 5, 6])
    with pytest.raises(mathex.VectorSpaceInitException):
        vec.VectorSpace([v1, v2, v3])


def test_basis_scalar_product():
    v1 = vec.Vector([[1, 2, 3]])
    v2 = vec.Vector([2, 3, 4])
    v3 = vec.Vector([1, 2, 0])
    vs = vec.VectorSpace([v1, v2, v3])
    x = vec.Vector([1, 4, 5])
    y = vec.Vector([2, 3, 6])
    res = vs.scalar_product(x, y)
    ans = 1138
    act = res == ans
    assert act


def test_point_in_basis():
    v1 = vec.Vector([[1, 1, 1]])
    v2 = vec.Vector([1, 0, 0])
    v3 = vec.Vector([0, 0, 1])
    p = vec.Point([2, 1, 2])
    vs = vec.VectorSpace([v1, v2, v3])
    res = vs.as_vector(p)
    ans = vec.Vector([1, 1, 1])
    act = res == ans
    assert act
