import geometry
import itertools

def print_approximations(p0, F, h0):
    epsilon = 1e-8
    pCur, fCur, hCur = p0, F(p0, h0), h0
    icycle = itertools.cycle(range(len(p0)))
    i, s = next(icycle), 0
    for k in itertools.count():
        print("x{0}: {1:.4f}, y{0}: {2:.4f}, r{0}: {3:.4f}, h: {4:.4f}, F{0}: {F:.4f}".format(k, *pCur, hCur, F=fCur))

        # Evaluate partial derivative of the objective function w.r.t. the i-th coordinate
        # at current point by finite differences.
        dp = [0] * len(p0)
        dp[i] += epsilon
        diF = F(geometry.add(pCur, dp), hCur) - fCur

        step = [0] * len(p0)
        step[i] -= diF if i != 2 else max(diF, -p0[i] * epsilon)
        step[i] /= epsilon

        pOld, fOld = pCur, fCur

        pCur = geometry.add(pOld, step)
        fCur = F(pCur, hCur)

        if i == 2 and fCur > fOld:
            pCur, fCur = pOld, fOld
            hCur *= 0.1
            if hCur < 0.001:
                break
            else:
                continue

        if (i == 2) or (abs((fCur - fOld) / fCur) < 0.001):
            i, s = next(icycle), k
    print("x*: {0:.4f}, y*: {1:.4f}, r*: {2:.4f}, h: {3:.4f}, F*: {F:.4f}".format(*pCur, hCur, F=fCur))
