import numpy as np


def grad(x):
    return np.array(np.gradient(x))


def norm(x, axis=0):
    return np.sqrt(np.sum(np.square(x), axis=axis))


def levelset(phi_0, g, tms, it):
    for k in range(it):
        phi_0 = phi_0 + tms * g * norm(grad(phi_0))
    return phi_0
