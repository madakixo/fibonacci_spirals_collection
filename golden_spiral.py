import numpy as np
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5)) / 2
b = np.log(phi) / (2 * np.pi)

theta = np.linspace(0, 12 * 2 * np.pi, 2000)
r = np.exp(b * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(8,8), facecolor='black')
plt.plot(x, y, color='gold', lw=1.8)
plt.axis('equal')
plt.axis('off')
plt.show()
