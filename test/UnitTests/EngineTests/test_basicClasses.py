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

