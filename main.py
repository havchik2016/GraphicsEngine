import lib.Math.LowLevelMath.matrixOperations as mtx
import lib.Math.LowLevelMath.vectorOperations as vec
import lib.Engine.BasicClasses.basicClasses as bc

if __name__ == "__main__":
    vec1 = vec.Vector([1, 0, 0])
    vec2 = vec.Vector([0, 1, 0])
    vec3 = vec.Vector([0, 0, 1])
    pt = vec.Point([0, 0, 0])
    vs = vec.VectorSpace([vec1, vec2, vec3])
    cs = vec.CoordinateSystem(pt, vs)
    ent = bc.Entity(cs)
    ent.biba = 2
    ent.remove_property("biba")
