import lib.Math.LowLevelMath.matrixOperations as mtx
import lib.Exceptions.MathExceptions.mathExceptions as mathex
import lib.Math.LowLevelMath.vectorOperations as vec
import pytest
from math import pi, sin, cos, sqrt


def test_non_positive_square_init():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix(-1)


def test_non_positive_first_argument_init():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix(-1, 2)


def test_non_positive_second_argument_init():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix(2, -1)


def test_non_emptiness():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix([])


def test_equal_row_lengths():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix([[2, 3.5], [1]])


def test_all_items_are_numbers():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix([[2, 3.5], [1, 'a']])


def test_illegal_init():
    with pytest.raises(mathex.MatrixInitException):
        m = mtx.Matrix("string lol")


def test_square_init():
    m = mtx.Matrix(3)
    lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    act = m.elements == lst

    assert act


def test_general_init():
    m = mtx.Matrix(2, 3)
    lst = [[0, 0, 0], [0, 0, 0]]

    act = m.elements == lst

    assert act


def test_element_init():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    lst = [[2, 1], [3.5, -1]]

    act = m.elements == lst

    assert act


def test_non_equality():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[2, 3], [3.5, -1]])

    act = m != n

    assert act


def test_equality():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[2, 1], [3.5, -1]])

    act = m == n

    assert act


def test_add_matrix_to_non_matrix():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    a = 2
    with pytest.raises(mathex.MatrixOperationException):
        res = m + 2


def test_adding_two_matrices_of_different_row_sizes():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[2, 5]])
    with pytest.raises(mathex.MatrixOperationException):
        res = m + n


def test_adding_two_matrices_of_different_col_sizes():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[2], [3.5]])
    with pytest.raises(mathex.MatrixOperationException):
        res = m + n


def test_good_addition():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[0, 2], [-5, 7]])
    r = mtx.Matrix([[2, 3], [-1.5, 6]])

    act = m + n == r

    assert act


def test_good_sub():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[0, 2], [-5, 7]])
    r = mtx.Matrix([[2, -1], [8.5, -8]])

    act = m - n == r

    assert act


def test_not_ok_size_mult():
    m = mtx.Matrix([[2, 1], [3.5, -1]])
    n = mtx.Matrix([[2, 1]])
    with pytest.raises(mathex.MatrixOperationException):
        res = m * n


def test_mult_two_matrices():
    m = mtx.Matrix([[2, 3, 4]])
    n = mtx.Matrix([[1, 2], [3, 4], [5, 6]])
    r = mtx.Matrix([[31, 40]])

    act = m * n == r

    assert act


def test_mult_matrix_by_number():
    m = mtx.Matrix([[2, 4], [6, -8]])
    num = 2.5
    n = mtx.Matrix([[5, 10], [15, -20]])

    act = m * num == n

    assert act


def test_left_mult_matrix_by_number():
    m = mtx.Matrix([[2, 4], [6, -8]])
    num = 2.5
    n = mtx.Matrix([[5, 10], [15, -20]])

    act = num * m == n

    assert act


def test_identity():
    m = mtx.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    n = 3
    r = mtx.Matrix.identity(n)

    act = m == r

    assert act


def test_non_list_minor():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rows = [1]
    cols = 2
    with pytest.raises(mathex.MatrixOperationException):
        res = m.get_minor(rows, cols)


def test_non_integer_minor():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rows = [1, 2]
    cols = [0.5]
    with pytest.raises(mathex.MatrixOperationException):
        res = m.get_minor(rows, cols)


def test_out_of_bounds_minor():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rows = [1, 3]
    cols = [0]
    with pytest.raises(mathex.MatrixOperationException):
        res = m.get_minor(rows, cols)


def test_non_unique_minor():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rows = [1, 1]
    cols = [2]
    with pytest.raises(mathex.MatrixOperationException):
        res = m.get_minor(rows, cols)


def test_get_minor():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rows = [1]
    cols = [0]
    r = mtx.Matrix([[2, 3], [8, 9]])
    print(m.get_minor(rows, cols).elements)
    act = m.get_minor(rows, cols) == r

    assert act


def test_non_square_determinant():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6]])
    res = m.determinant()
    ans = 0
    act = res == ans
    assert act


def test_zero_determinant():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    det = m.determinant()
    res = 0
    act = det == res
    assert act


def test_nonzero_determinant():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 8]])
    det = m.determinant()
    res = 3
    act = det == res
    assert act


def test_non_square_inverse():
    m = mtx.Matrix([[1, 2]])
    with pytest.raises(mathex.MatrixOperationException):
        m.inverse()


def test_zero_determinant_inverse():
    m = mtx.Matrix([[1, 2], [2, 4]])
    with pytest.raises(mathex.MatrixOperationException):
        m.inverse()


def test_nonzero_determinant_inverse():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 8]])
    res = m.inverse()
    ans = mtx.Matrix([[-8 / 3, 8 / 3, -1], [10 / 3, -13 / 3, 2], [-1, 2, -1]])
    act = True
    for i in range(3):
        for j in range(3):
            act &= (abs(res.elements[i][j] - ans.elements[i][j]) < 1e-6)
    assert act


def test_transpose():
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6]])
    res = m.transpose()
    ans = mtx.Matrix([[1, 4], [2, 5], [3, 6]])
    act = res == ans
    assert act


def test_matrix_div():
    a = mtx.Matrix.identity(3)
    m = mtx.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 8]])
    res = m.inverse()
    act = (a / m) == res
    assert act


def test_zero_div():
    m = mtx.Matrix.identity(3)
    with pytest.raises(mathex.MatrixOperationException):
        res = m / 0


def test_nonzero_div():
    m = mtx.Matrix.identity(3)
    res = mtx.Matrix([[1 /2, 0, 0], [0, 1 / 2, 0], [0, 0, 1 / 2]])
    act = (m / 2) == res
    assert act


def test_gram():
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([1, 0, 0])
    v3 = vec.Vector([0, 2, 0])
    res = mtx.Matrix.gram(v1, v2, v3)
    ans = mtx.Matrix([[14, 1, 4], [1, 1, 0], [4, 0, 4]])
    act = res == ans
    assert act


def test_illegal_gram():
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([4, 5, 6])
    v3 = 2
    with pytest.raises(Exception):
        mtx.Matrix.gram(v1, v2, v3)


def test_rotation_matrix():
    inds = (0, 2)
    n = 4
    angle = pi / 4
    res = mtx.Matrix.get_rotation_matrix(inds, angle, n)
    ans = mtx.Matrix([[cos(angle), 0, sin(angle), 0],
                      [0, 1, 0, 0],
                      [-sin(angle), 0, cos(angle), 0],
                      [0, 0, 0, 1]])
    act = res == ans
    assert act


def test_teit_bryan_matrix():
    angles = (pi / 3, 2 * pi / 3, pi / 4)
    res = mtx.Matrix.get_teit_bryan_matrix(angles)
    m1 = mtx.Matrix([[1, 0, 0],
                      [0, cos(angles[0]), -sin(angles[0])],
                      [0, sin(angles[0]), cos(angles[0])]])
    m2 = mtx.Matrix([[cos(angles[1]), 0, sin(angles[1])],
                     [0, 1, 0],
                     [-sin(angles[1]), 0, cos(angles[1])]])
    m3 = mtx.Matrix([[cos(angles[2]), -sin(angles[2]), 0],
                     [sin(angles[2]), cos(angles[2]), 0],
                     [0, 0, 1]])
    ans = m1 * m2 * m3
    act = res == ans
    assert act
