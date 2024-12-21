import numpy as np
from scipy.optimize import minimize
import optuna
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

# Objective function for Optuna trial.
def objective(trial):
    # Sample theta values within a specified range
    theta1 = trial.suggest_float('theta1', -np.pi, np.pi)
    theta2 = trial.suggest_float('theta2', -np.pi, np.pi)
    theta3 = trial.suggest_float('theta3', -np.pi, np.pi)
    theta4 = trial.suggest_float('theta4', -np.pi, np.pi)

    # Combine into a vector for the cost function
    theta_vec = [theta1, theta2, theta3, theta4]
    return cost_function(theta_vec, U, beta)

optuna.logging.set_verbosity(optuna.logging.WARNING)
time_start = time.time()

# Problem values
U = np.array([[0, -1], [1, 0]])  # Target SU(2) matrix
beta = np.pi / 4  # beta value

# Create a study for optimization
study = optuna.create_study(sampler=optuna.samplers.CmaEsSampler())
study.optimize(objective, n_trials=1000)

# Get the best trial results
best_trial = study.best_trial
print(f"Thetas: theta1={best_trial.params['theta1']}, "
      f"theta2={best_trial.params['theta2']}, "
      f"theta3={best_trial.params['theta3']}, "
      f"theta4={best_trial.params['theta4']}")
print(f"Cost: {best_trial.value}")
print(f"Time: {time.time() - time_start}")

# TODO: Here I only considered U. The case of -U should be included.