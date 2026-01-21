import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Golden ratio
phi = (1 + np.sqrt(5)) / 2

# Growth factor b = ln(phi) / (2 * pi)
b = np.log(phi) / (2 * np.pi)

# Parameters
a = 1  # initial radius scale
k = 0.5  # height scale per radian
theta_max = 20 * np.pi  # number of turns
theta = np.linspace(0, theta_max, 10000)

# Radius
r = a * np.exp(b * theta)

# Coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)
z = k * theta

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='goldenrod', linewidth=2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Golden Spiral using Golden Ratio and Pi')

# Show the plot
plt.show()

# Optionally save to file
# plt.savefig('golden_spiral_3d.png')
