import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# ────────────────────────────────────────────────
#   Golden spiral – 12 Hijri months metaphor
#   Fixed version – no overflow in exp()
# ────────────────────────────────────────────────

# Golden ratio & growth constant
phi = (1 + np.sqrt(5)) / 2
b = np.log(phi) / (2 * np.pi)

# ─── Parameters ──────────────────────────────────
a = 0.7                     # starting radius scale
height_per_radian = 0.085   # z growth per radian

REVOLUTIONS_PER_DAY = 23.75      # ≈ lunar day
REVOLUTIONS_PER_HOUR = 1.0

# Hijri months (stylized day counts)
hijri_months = [
    "Muharram", "Safar", "Rabi' al-Awwal", "Rabi' al-Thani",
    "Jumada al-Awwal", "Jumada al-Thani", "Rajab", "Sha'ban",
    "Ramadan", "Shawwal", "Dhu al-Qa'dah", "Dhu al-Hijjah"
]

days_per_month = np.array([29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30])

# ─── Safety limits to prevent overflow ───────────
MAX_THETA_RAD = 80 * np.pi          # ≈ 40 full turns – adjust higher only if needed
MAX_RADIUS = 300.0                  # hard cap on radius (units)

# ─── Build theta with variable density ───────────

theta_segments = []
current_theta = 0.0
month_boundaries = [0]

for month_idx, days in enumerate(days_per_month):
    rev_this_month = days * REVOLUTIONS_PER_DAY
    points_per_rev = 28 + (month_idx % 3)   # 28,29,30 cycling

    n_points = int(rev_this_month * points_per_rev) + 1

    theta_month = np.linspace(
        current_theta,
        current_theta + rev_this_month * 2 * np.pi,
        n_points,
        endpoint=False
    )

    # Safety: clip theta early
    theta_month = np.minimum(theta_month, MAX_THETA_RAD)

    theta_segments.append(theta_month)
    current_theta += rev_this_month * 2 * np.pi
    month_boundaries.append(len(np.concatenate(theta_segments)))

theta = np.concatenate(theta_segments)

# ─── Coordinates with overflow protection ────────

r = a * np.exp(b * theta)
r = np.clip(r, 0, MAX_RADIUS)                   # prevent infinity
r = np.nan_to_num(r, nan=0.0, posinf=MAX_RADIUS, neginf=0.0)

x = r * np.cos(theta)
y = r * np.sin(theta)
z = height_per_radian * theta

# ─── Colors per month ─────────────────────────────

month_colors = plt.cm.tab20(np.linspace(0, 1, 12))
colors = np.zeros((len(theta), 4))

for m in range(12):
    start = month_boundaries[m]
    end   = month_boundaries[m+1] if m+1 < len(month_boundaries) else len(theta)
    colors[start:end] = month_colors[m]

# ─── Day markers (every ~23.75 rev) ───────────────

day_marker_theta = []
current_rev = 0.0
step_rev = 1.0

while current_rev < theta.max() / (2 * np.pi):
    if current_rev % REVOLUTIONS_PER_DAY < step_rev / 2:
        idx = np.argmin(np.abs(theta - current_rev * 2 * np.pi))
        if idx < len(theta):  # safety
            day_marker_theta.append(theta[idx])
    current_rev += step_rev

day_theta = np.array(day_marker_theta)
day_r = a * np.exp(b * day_theta)
day_r = np.clip(day_r, 0, MAX_RADIUS)
day_x = day_r * np.cos(day_theta)
day_y = day_r * np.sin(day_theta)
day_z = height_per_radian * day_theta

# ─── Plot ────────────────────────────────────────

fig = plt.figure(figsize=(13, 11))
ax = fig.add_subplot(111, projection='3d')

# Spiral line
line, = ax.plot(x, y, z, lw=1.4, color='goldenrod', alpha=0.88)

# Day markers (small glowing points)
day_scatter = ax.scatter(day_x, day_y, day_z,
                         c='white', s=20, alpha=0.7,
                         edgecolor='lime', linewidth=0.8,
                         zorder=10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (Time)')

total_days = np.sum(days_per_month)
ax.set_title(
    f"Golden Spiral – Hijri Calendar Metaphor\n"
    f"12 months • {total_days} days • {REVOLUTIONS_PER_DAY:.2f} rev/day\n"
    f"Growth factor φ ≈ {phi:.8f} • radius capped at {MAX_RADIUS}",
    fontsize=13, pad=20
)

# Set reasonable limits
max_r = np.max(r) * 1.15
ax.set_xlim(-max_r, max_r)
ax.set_ylim(-max_r, max_r)
ax.set_zlim(0, np.max(z) * 1.1)

ax.grid(True, alpha=0.1)

# ─── Animation – rotating view ───────────────────

def update(frame):
    elev = 20 + 8 * np.sin(frame * 0.04)
    azim = -60 + frame * 0.9
    ax.view_init(elev=elev, azim=azim)
    return line, day_scatter

ani = animation.FuncAnimation(fig, update, frames=400,
                              interval=40, blit=False)

plt.tight_layout()
plt.show()

# To save as video (requires ffmpeg installed):
# ani.save('hijri_golden_spiral.mp4', writer='ffmpeg', fps=30, dpi=120)
