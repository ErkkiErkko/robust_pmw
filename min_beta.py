import numpy as np
from scipy.optimize import minimize
import time
import gen_su2

# Returns the Z rotation matrix Z_theta.
def Z(theta):
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp(1j * theta / 2)]])

# Returns the X_beta matrix.
def X(beta):
    return np.array([[np.cos(beta / 2), -1j * np.sin(beta / 2)],
                     [-1j * np.sin(beta / 2), np.cos(beta / 2)]])

# Computes the matrix X_beta(theta).
def shifted_X(theta, beta):
    return Z(-theta) @ X(beta) @ Z(theta)

# Computes the product of rotation matrices.
def product_of_rotations(theta_vec, beta):
    theta1, theta2, theta3, theta4 = theta_vec
    return shifted_X(theta1, beta) @ shifted_X(theta2, beta) @ shifted_X(theta3, beta) @ shifted_X(theta4, beta)

# Cost function for optimization.
def cost_function(theta_vec, U, beta):
    F = product_of_rotations(theta_vec, beta)
    return np.linalg.norm(F - U)**2  # Frobenius norm

time_start = time.time()

# Problem values
# U = np.array([[0, -1], [1, 0]])  # Target SU(2) matrix
U = gen_su2.random_su2()
eps = 1e-15

print(U)

time_start = time.time()

l = 0
r = np.pi / 2  # max beta value
ans_beta = 0
ans_theta = []
ans_cost = 0

while l + eps < r:
    # print(f"{l}, {r}")
    beta = (l + r) / 2
    initial_guess = [0, 0, 0, 0]  # Initial guess for the angles
    result0 = minimize(cost_function, initial_guess, args=(U, beta), tol=eps, options={'maxiter': 1000})
    result1 = minimize(cost_function, initial_guess, args=(-U, beta), tol=eps, options={'maxiter': 1000})

    if cost_function(result0.x, U, beta) < eps:
        ans_beta = beta
        ans_theta = result0.x
        ans_cost = cost_function(result0.x, U, beta)
        r = beta
    elif cost_function(result1.x, -U, beta) < eps:
        ans_beta = beta
        ans_theta = result1.x
        ans_cost = cost_function(result1.x, -U, beta)
        r = beta
    else:
        l = beta

theta1, theta2, theta3, theta4 = ans_theta
print(f"Beta: {ans_beta}")
print(f"Thetas: {theta1}, {theta2}, {theta3}, {theta4}")
print(f"Cost: {ans_cost}")
print(f"Time: {time.time() - time_start}")