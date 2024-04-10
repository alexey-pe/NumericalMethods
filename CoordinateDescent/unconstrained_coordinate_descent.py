import geometry
import itertools

def print_approximations(p0, Z):
    epsilon = 1e-8
    pCur, zCur = p0, Z(p0)
    icycle = itertools.cycle(range(len(p0)))
    i, s = next(icycle), 0
    for k in itertools.count():
        print("x{0}: {1:.4f}, y{0}: {2:.4f}, r{0}: {3:.4f}, z{0}: {z:.4f}, evaluations: {4}".format(k, *pCur, zCur * zCur / 3, 1 + 2 * k, z=zCur))

        # Evaluate partial derivative of the objective function w.r.t. the i-th coordinate
        # at current point by finite differences.
        dp = [0] * len(p0)
        dp[i] += epsilon
        diZ = Z(geometry.add(pCur, dp)) - zCur

        step = [0] * len(p0)
        step[i] -= diZ
        step[i] /= epsilon

        pOld, zOld = pCur, zCur

        pCur = geometry.add(pOld, step)
        zCur = Z(pCur)

        if abs((zCur - zOld) / zCur) < 0.001:
            if k - s < 2:
                break
            i, s = next(icycle), k
    print("x*: {0:.4f}, y*: {1:.4f}, r*: {2:.4f}, z*: {z:.4f}, evaluations: {3}".format(*pCur, zCur * zCur / 3, 1 + 2 * (k + 1), z=zCur))
