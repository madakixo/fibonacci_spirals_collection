import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ────────────────────────────────────────────────
#  Settings – 360 revolutions in 12 cycles
# ────────────────────────────────────────────────

TOTAL_REVOLUTIONS = 360
CYCLES = 12

# Number of points per revolution in each group of cycles
points_per_rev = np.array([28] * 4 + [29] * 4 + [30] * 4)

# Golden ratio & logarithmic growth constant
phi = (1 + np.sqrt(5)) / 2           # ≈ 1.6180339887
b = np.log(phi) / (2 * np.pi)        # growth rate per radian

# Base parameters
a = 0.8               # starting radius scale
height_per_radian = 0.12   # z growth per radian (controls stretch)

# ────────────────────────────────────────────────
#  Build angle array with variable density
# ────────────────────────────────────────────────

theta_segments = []
current_theta = 0.0

for cycle in range(CYCLES):
    n_points = points_per_rev[cycle]
    rev_angle = 2 * np.pi * TOTAL_REVOLUTIONS / CYCLES
    
    # linspace for this cycle
    theta_cycle = np.linspace(
        current_theta,
        current_theta + rev_angle,
        n_points,
        endpoint=False   # avoid duplicating point at junction
    )
    theta_segments.append(theta_cycle)
    current_theta += rev_angle

# Concatenate all segments
theta = np.concatenate(theta_segments)

# Radius grows exponentially with angle (golden spiral law)
r = a * np.exp(b * theta)

# Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)
z = height_per_radian * theta

# ────────────────────────────────────────────────
#  Plot
# ────────────────────────────────────────────────

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Main spiral
ax.plot(x, y, z,
        color='goldenrod',
        linewidth=1.4,
        alpha=0.92)

# Optional: color by height (prettier)
# colors = plt.cm.viridis(z / z.max())
# ax.scatter(x, y, z, c=colors, s=2, alpha=0.6)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'3D Golden Spiral – {TOTAL_REVOLUTIONS} revolutions in {CYCLES} cycles\n'
             f'(28–29–30 points/rev)   •   growth factor φ ≈ {phi:.8f}')

# Make it look nicer
ax.view_init(elev=18, azim=135)
ax.grid(True, alpha=0.15)

plt.tight_layout()
plt.show()

# Optional: save high-resolution image
# plt.savefig("golden_spiral_360rev_12cycles.png", dpi=300, bbox_inches='tight')
