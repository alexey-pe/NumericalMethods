from math import sqrt

def point_segment_distance2(p, v1, v2):
    s = subtract(p, v1)
    v = subtract(v2, v1)
    n = subtract(s, proj(s, v))
    return norm2(n)


def add(v1, v2):
    return tuple(u1 + u2 for u1, u2 in zip(v1, v2))


def subtract(v2, v1):
    return tuple(u1 - u2 for u1, u2 in zip(v1, v2))


def proj(w, v):
    vn = normed(v)
    p = dot_product(w, vn)
    return scale(vn, p)


def normed(v):
    length = sqrt(norm2(v))
    return v[0] / length, v[1] / length


def norm2(v):
    return dot_product(v, v)


def dot_product(w, v):
    return w[0] * v[0] + w[1] * v[1]


def scale(v, s):
    return v[0] * s, v[1] * s
