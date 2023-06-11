import lib.Math.LowLevelMath.matrixOperations as mtx
import lib.Math.LowLevelMath.vectorOperations as vec

if __name__ == "__main__":
    matrix1 = mtx.Matrix([[1, 0, 1], [0, 1, 2]])
    matrix2 = mtx.Matrix([[-1, 2], [0, 1], [2, -3]])
    matrix3 = matrix1 * matrix2  # Matrix ([[1 , -1] , [4 , -5]])
    matrix4 = matrix2 * matrix3  # Matrix ([[ -1 , 2 , 3] , [0 , 1 , 2] , [2 , -3 , -4]])
    print(matrix3.determinant(), matrix4.determinant())
