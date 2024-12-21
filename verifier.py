import numpy as np

# Define rotation matrices
def x_rotation(theta):
    """Returns the Z rotation matrix for angle theta."""
    return np.matrix([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                       [-1j * np.sin(theta / 2), np.cos(theta / 2)]])

def z_rotation(phi):
    """Returns the X rotation matrix for angle phi."""
    return np.matrix([[np.exp(-1j * phi / 2), 0],
                       [0, np.exp(1j * phi / 2)]])

def shifted_x(sigma, phi):
    return z_rotation(-phi) * x_rotation(sigma) * z_rotation(phi)

# Problem value
beta = 1.4381049003206545
theta_1, theta_2, theta_3, theta_4 = [-0.97964217, -1.21931343, -1.43457189, -1.69154543]

# Perform the calculation
result = shifted_x(beta, theta_1) * shifted_x(beta, theta_2) * shifted_x(beta, theta_3) * shifted_x(beta, theta_4)

# Print the result
print(result)