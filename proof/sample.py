import numpy as np
import matplotlib.pyplot as plt

# Define k for the given scenario
beta = np.arccos(np.sqrt(1.0/(4+2*np.sqrt(2))))*2 - 0.05
# beta = np.arccos(np.sqrt(np.sqrt(2.0)/(1+np.sqrt(2))))*2
k_new_sqrt2 = np.cos(beta/2)**2

# Define s(u) for the general formula
def s_u_general(u, k):
    return (k - (1 - k)*u)**2

# Define r(u) = k * (1 - k) * |1 + u|^2
def r_u(u, k):
    return k * (1 - k) * abs(1 + u)**2

# Define unit circle
u_values = np.exp(1j * np.linspace(0, 2*np.pi, 400))
s_values_new_k_sqrt2 = s_u_general(u_values, k_new_sqrt2)

# Sample a few values of u on the unit circle for drawing the circles
sampled_u = np.exp(1j * np.linspace(0, 2*np.pi, 16))
sampled_s = s_u_general(sampled_u, k_new_sqrt2)
sampled_r = r_u(sampled_u, k_new_sqrt2)

# Plot the path of s(u)
plt.figure(figsize=(6, 6))
plt.plot(s_values_new_k_sqrt2.real, s_values_new_k_sqrt2.imag, label=rf"$s(u) = \left({k_new_sqrt2:.3f} - (1 - {k_new_sqrt2:.3f})u\right)^2$", color='blue')

# Plot circles for sampled s(u) with radius r(u)
for i, (center, radius) in enumerate(zip(sampled_s, sampled_r)):
    circle = plt.Circle((center.real, center.imag), radius, color='orange', fill=False, linestyle='--', label=f'Circle {i+1}' if i == 0 else "")
    plt.gca().add_artist(circle)
    
# Mark the sampled centers with points
plt.scatter(sampled_s.real, sampled_s.imag, color='red', zorder=5)

# Define the unit circle for plotting
unit_circle = np.exp(1j * np.linspace(0, 2*np.pi, 400))

# Plot the unit circle
plt.plot(unit_circle.real, unit_circle.imag, 'g--', label='Unit Circle')

# Label and plot settings
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title(r'Path of $s(u)$ in the Complex Plane with Circles for beta=' + str(beta))
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.show()
