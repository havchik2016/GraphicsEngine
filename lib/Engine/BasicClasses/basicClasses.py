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
        self.value = Identifier.__generate__(self)

    def __generate__(self):
        new_val = random.randrange(0, 2 ** 64)
        while new_val in self.identifiers:
            new_val = random.randrange(0, 2 ** 64)
        self.identifiers.add(new_val)
        return new_val

    def get_value(self):
        return self.value


class Entity:
    def __init__(self, cs: vec.CoordinateSystem):
        if not isinstance(cs, vec.CoordinateSystem):
            raise engex.EntityException("Entity has to be initialized with a coordinate system!")
        self.cs = cs
        self.identifier = Identifier().get_value()
        self.properties = dict()

    def set_property(self, prop: str, value):
        if not isinstance(prop, str):
            raise engex.EntityException("Property names must be strings!")
        self.properties[prop] = value

    def get_property(self, prop: str):
        if not isinstance(prop, str):
            raise engex.EntityException("Property names must be strings!")
        return self.properties[prop]

    def remove_property(self, prop: str):
        if not isinstance(prop, str):
            raise engex.EntityException("Property names must be strings!")
        if prop not in self.properties.keys():
            raise engex.EntityException("Property must exist to be deleted!")
        del self.properties[prop]

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise engex.EntityException("Property names must be strings!")
        if item not in self.properties.keys():
            raise engex.EntityException("Property must exist to get its value!")
        return self.properties[item]

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise engex.EntityException("Property names must be strings!")
        self.properties[key] = value

