import numpy as np
import matplotlib.pyplot as plt

# Define k for the given scenario
beta = np.arccos(np.sqrt(1.0/(4+2*np.sqrt(2))))*2 - 0.05
k_new_sqrt2 = np.cos(beta/2)**2

# Define s(u) for the general formula
def s_u_general(u, k):
    return (k - (1 - k)*u)**2

# Define unit circle
u_values = np.exp(1j * np.linspace(0, 2*np.pi, 400))
s_values_new_k_sqrt2 = s_u_general(u_values, k_new_sqrt2)

# Define the unit circle for plotting
unit_circle = np.exp(1j * np.linspace(0, 2*np.pi, 400))

# Plot the path of s(u)
plt.figure(figsize=(6, 6))
plt.plot(s_values_new_k_sqrt2.real, s_values_new_k_sqrt2.imag, label=rf"$s(u) = \left({k_new_sqrt2:.3f} - (1 - {k_new_sqrt2:.3f})u\right)^2$", color='blue')

# Plot the unit circle
plt.plot(unit_circle.real, unit_circle.imag, 'g--', label='Unit Circle')

# Label and plot settings
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title(f'Path of $s(u)$ with Unit Circle for beta=' + str(beta))
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()