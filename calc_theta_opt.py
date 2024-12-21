import numpy as np
from scipy.optimize import minimize
import time

# Returns the Z rotation matrix Z_theta.
def Z(theta):
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp(1j * theta / 2)]])

# Returns the X matrix.
def X(beta):
    return np.array([[np.cos(beta / 2), -1j * np.sin(beta / 2)],
                     [-1j * np.sin(beta / 2), np.cos(beta / 2)]])

# Computes the matrix X(theta).
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
U = np.array([[-0.85545599-0.46362917j, -0.22225151-0.06202673j],
 [ 0.22225151-0.06202673j, -0.85545599+0.46362917j]])  # Target SU(2) matrix
beta = 1.423534171157875 # beta value

initial_guess = [0, 0, 0, 0]  # Initial guess for the angles
result0 = minimize(cost_function, initial_guess, args=(U, beta), tol=1e-15, options={'maxiter': 1000})
result1 = minimize(cost_function, initial_guess, args=(-U, beta), tol=1e-15, options={'maxiter': 1000})

if cost_function(result0.x, U, beta) < 1e-13:
    theta1, theta2, theta3, theta4 = result0.x
    print(f"Optimized angles: {theta1}, {theta2}, {theta3}, {theta4}")
    print(f"Best cost: {cost_function(result0.x, U, beta)}")
elif cost_function(result1.x, -U, beta) < 1e-13:
    theta1, theta2, theta3, theta4 = result1.x
    print(f"Optimized angles: {theta1}, {theta2}, {theta3}, {theta4}")
    print(f"Best cost: {cost_function(result1.x, -U, beta)}")
else:
    print("Calculation failed.")

print(f"Time: {time.time() - time_start}")