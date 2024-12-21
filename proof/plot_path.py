import numpy as np
import matplotlib.pyplot as plt

# Given constant
a = 0.7524301913829837
theta = np.linspace(0, 2 * np.pi, 1000)
u = np.exp(1j * theta)

# Calculate s(u)
s_u = (a**2 - (1 - a**2) * u)**2

# Plot the path of s(u)
plt.figure(figsize=(6,6))
plt.plot(s_u.real, s_u.imag)
plt.title(r"Path of $s(u) = (a^2 - (1 - a^2)u)^2$ where $|u| = 1$")
plt.xlabel('Re($s(u)$)')
plt.ylabel('Im($s(u)$)')
plt.axis('equal')
plt.grid(True)
plt.show()