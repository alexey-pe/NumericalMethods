import geometry
import itertools

def print_approximations(p0, Z):
    epsilon = 1e-8
    pCur, zCur = p0, Z(p0)


    for k in itertools.count():
        print("x{0}: {1:.4f}, y{0}: {2:.4f}, r{0}: {3:.4f}, z{0}: {z:.4f}, evaluations: {4}".format(k, *pCur, zCur * zCur / 3, 1 + 3 * k, z=zCur))

        # Evaluate antigradient of the objective function
        # at current point by finite differences.
        dx, dy = (epsilon, 0.0), (0.0, epsilon)
        dxZ = Z(geometry.add(pCur, dx)) - zCur
        dyZ = Z(geometry.add(pCur, dy)) - zCur

        antigradient = [-dxZ, -dyZ]
        antigradient[0] /= epsilon
        antigradient[1] /= epsilon

        pOld, zOld = pCur, zCur

        pCur = geometry.add(pOld, antigradient)
        zCur = Z(pCur)

        if abs((zCur - zOld) / zCur) < 0.001:
            break


    print("x*: {0:.4f}, y*: {1:.4f}, r*: {2:.4f}, z*: {z:.4f}, evaluations: {3}".format(*pCur, zCur * zCur / 3, 1 + 3 * (k + 1), z=zCur))
