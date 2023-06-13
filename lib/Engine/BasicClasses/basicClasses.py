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
        self.identifier = Identifier()
        self.properties = dict()

    def set_property(self, prop: str, value):
        if not isinstance(prop, str):
            raise engex.EntityException("Property names must be strings!")
        self.properties[prop] = value

    def get_property(self, prop: str):
        if not isinstance(prop, str):
            raise engex.EntityException("Property names must be strings!")
        if prop not in self.properties.keys():
            raise engex.EntityException("Property must exist to be deleted!")
        return self.properties[prop]

    def remove_property(self, prop: str):
        if not isinstance(prop, str):
            raise engex.EntityException("Property names must be strings!")
        if prop not in self.properties.keys():
            raise engex.EntityException("Property must exist to be deleted!")
        del self.properties[prop]

    def __getitem__(self, item):
        return self.get_property(item)

    def __setitem__(self, key, value):
        self.set_property(key, value)


class EntitiesList:
    def __init__(self, entities: list):
        if not isinstance(entities, list) or not all(isinstance(e, Entity) for e in entities):
            raise engex.EntitiesListException("You must give a list of entities!")
        self.entities = entities

    def append(self, entity: Entity):
        if not isinstance(entity, Entity):
            raise engex.EntitiesListException("Only Entity objects can be added!")
        self.entities.append(entity)

    def remove(self, entity: Entity):
        if not isinstance(entity, Entity):
            raise engex.EntitiesListException("Only Entity objects can be deleted!")
        for (i, e) in enumerate(self.entities):
            if e.identifier.get_value() == entity.identifier.get_value():
                self.entities = self.entities[:i] + self.entities[i + 1:]
                return
        raise engex.EntitiesListException("Entity must exist to be deleted!")

    def get(self, id: Identifier) -> Entity:
        if not isinstance(id, Identifier):
            raise engex.EntitiesListException("You can only get Entity objects by an Identifier object!")
        for e in self.entities:
            if e.identifier.get_value() == id.get_value():
                return e
        raise engex.EntitiesListException("Entity with given id must exist to be returned!")

    def exec(self, func):
        for (i, e) in self.entities:
            self.entities[i] = func(self.entities[i])

    def __getitem__(self, item):
        self.get(item)

