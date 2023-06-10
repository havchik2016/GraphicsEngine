import lib.Math.LowLevelMath.matrixOperations as mtx
import lib.Math.LowLevelMath.vectorOperations as vec

if __name__ == "__main__":
    v1 = vec.Vector([1, 2, 3])
    v2 = vec.Vector([2, 3, 4])
    v3 = vec.Vector([1, 2, 0])
    m = mtx.Matrix.gram(v1, v2, v3)
    x = vec.Vector([1, 4, 5])
    y = vec.Vector([2, 3, 6])
    print(m.elements)
    print(x.elements)
    print(y.elements)
    print((x * m * y.transpose()).elements)
