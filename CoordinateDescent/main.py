from geometry import point_segment_distance2
from math import sqrt

import unconstrained_gradient_descent
import unconstrained_coordinate_descent
import constrained_coordinate_descent

q = [(1 - sqrt(3), 0.0), (1 + sqrt(3), 0.0), (1.0, 3.0)]


def side_distances2(p):
    for i, j in zip(range(0, 3), range(1, 4)):
        j %= len(q)
        n2 = point_segment_distance2(p, q[i], q[j])
        # print(i, j, sqrt(n2))
        yield n2


def Z(p):
    return sqrt(sum(side_distances2(p)))


def F(u, h):
    p, r = u[0:-1], u[-1]
    return -r + sum(h / (sqrt(d2) - r) for d2 in side_distances2(p))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # unconstrained_gradient_descent.print_approximations((0.0, 0.5), Z)
    # unconstrained_coordinate_descent.print_approximations((0.0, 0.5), Z)
    constrained_coordinate_descent.print_approximations([0.0, 0.5, 0.1], F, 0.05)

