import lib.Engine.BasicClasses.basicClasses as bc
import lib.Math.LowLevelMath.vectorOperations as vec
import lib.Exceptions.EngineExceptions.engineExceptions as engex
import pytest


def test_identifier():
    res = bc.Identifier().get_value()
    assert res is not None


def test_property_methods():
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt = vec.Point([0, 0, 0])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs = vec.CoordinateSystem(pt, vs)
    ent = bc.Entity(cs)
    ent.set_property("biba", 2)
    res = ent.get_property("biba")
    ans = 2
    act = res == ans
    assert act


def test_overloaded_property_methods():
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt = vec.Point([0, 0, 0])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs = vec.CoordinateSystem(pt, vs)
    ent = bc.Entity(cs)
    ent["biba"] = 2
    res = ent["biba"]
    ans = 2
    act = res == ans
    assert act


def test_non_existing_deletion():
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt = vec.Point([0, 0, 0])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs = vec.CoordinateSystem(pt, vs)
    ent = bc.Entity(cs)
    ent["biba"] = 2
    with pytest.raises(engex.EntityException):
        ent.remove_property("lol")


def test_existing_deletion():
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt = vec.Point([0, 0, 0])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs = vec.CoordinateSystem(pt, vs)
    ent = bc.Entity(cs)
    ent["biba"] = 2
    ent.remove_property("biba")
    with pytest.raises(engex.EntityException):
        print(ent["biba"])


def test_entities_list_append():
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt1 = vec.Point([0, 0, 0])
    pt2 = vec.Point([1, 1, 1])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs1 = vec.CoordinateSystem(pt1, vs)
    ent1 = bc.Entity(cs1)
    cs2 = vec.CoordinateSystem(pt2, vs)
    ent2 = bc.Entity(cs2)
    entities = []
    eList = bc.EntitiesList(entities)
    eList.append(ent1)
    eList.append(ent2)
    res = eList.get(ent1.identifier).identifier.get_value()
    ans = ent1.identifier.get_value()
    act = res == ans
    assert act


def test_entities_list_remove_existing():
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt1 = vec.Point([0, 0, 0])
    pt2 = vec.Point([1, 1, 1])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs1 = vec.CoordinateSystem(pt1, vs)
    ent1 = bc.Entity(cs1)
    cs2 = vec.CoordinateSystem(pt2, vs)
    ent2 = bc.Entity(cs2)
    entities = []
    eList = bc.EntitiesList(entities)
    eList.append(ent1)
    eList.append(ent2)
    eList.remove(ent1)
    eList.get(ent2.identifier)
    with pytest.raises(engex.EntitiesListException):
        eList.get(ent1.identifier)
