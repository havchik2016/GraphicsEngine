import lib.Math.LowLevelMath.vectorOperations as vec
import lib.Exceptions.EngineExceptions.engineExceptions as engex
import random


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


class Identifier:
    identifiers = set()

    def __init__(self):
        self.value = Identifier.__generate__()

    def __generate__(self):
        new_val = random.randrange(0, 2 ** 64)
        while self.value in self.identifiers:
            new_val = random.randrange(0, 2 ** 64)
        self.identifiers.add(new_val)
        return new_val

    def get_value(self):
        return self.value


