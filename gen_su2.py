import numpy as np
import random

# Returns the Z rotation matrix Z_theta.
def Z(theta):
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp(1j * theta / 2)]])

# Returns the X_beta matrix.
def X(beta):
    return np.array([[np.cos(beta / 2), -1j * np.sin(beta / 2)],
                     [-1j * np.sin(beta / 2), np.cos(beta / 2)]])

# Returns a random SU(2) matrix.
def random_su2():
    phi = random.uniform(0, np.pi * 2)
    theta = random.uniform(0, np.pi * 2)
    lambd = random.uniform(0, np.pi * 2)
    return Z(phi) @ X(theta) @ Z(lambd)