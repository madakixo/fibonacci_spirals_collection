import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

phi = (1 + np.sqrt(5)) / 2
b = np.log(phi)/(2*np.pi)

theta = np.linspace(0, 20*np.pi, 4000)
r = np.exp(b * theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
z = theta * 0.4   # linear rise

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='gold', lw=1.6)

ax.set_box_aspect([1,1,1.6])
ax.axis('off')
plt.show()
