import lib.Math.LowLevelMath.vectorOperations as vec
import lib.Exceptions.EngineExceptions.engineExceptions as engex


class Ray:
    def __init__(self, cs: vec.CoordinateSystem, initialpt: vec.Point,
                 direction: vec.Vector):
        if not isinstance(cs, vec.CoordinateSystem) or \
                not isinstance(initialpt, vec.Point) \
                or not isinstance(direction, vec.Vector):
            raise engex.RayException("Illegal type arguments!")
        self.cs = cs
        self.initialpt = initialpt
        self.direction = direction
