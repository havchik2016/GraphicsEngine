class MathException(Exception):
    pass


class MatrixException(MathException):
    pass


class MatrixInitException(MatrixException):
    pass


class MatrixOperationException(MatrixException):
    pass


class VectorException(MatrixException):
    pass


class VectorSpaceException(MathException):
    pass


class VectorSpaceInitException(VectorSpaceException):
    pass


class VectorSpaceOperationException(VectorSpaceException):
    pass


class PointException(VectorException):
    pass