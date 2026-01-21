import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ────────────────────────────────────────────────
#   Calendar-inspired 3D golden spiral – FIXED
#   12 months → different number of days (28/29/30)
#   1 day = 24 revolutions (hours)
# ────────────────────────────────────────────────

# Golden ratio & growth constant
phi = (1 + np.sqrt(5)) / 2
b = np.log(phi) / (2 * np.pi)          # growth per radian

# ─── Safety limits to prevent overflow ───────────
MAX_THETA_RAD = 60 * np.pi             # ≈ 30 full turns – safe value
MAX_RADIUS    = 200.0                  # hard cap on radius

# ─── Parameters ──────────────────────────────────
a = 0.6                     # starting radius scale
height_per_radian = 0.09    # z growth per radian

REVOLUTIONS_PER_DAY = 24    # 1 day = 24 full turns (hours)

# Month lengths (in days) — grouped in pattern 28/29/30
days_per_month = np.array([
    28, 28, 29, 30,          # first quarter-year-ish
    29, 30, 28, 29,
    30, 28, 30, 29           # last months
])

# ─── Build theta (angle) array ───────────────────

theta_segments = []
current_theta = 0.0

for month_idx, days_in_month in enumerate(days_per_month):
    # revolutions this month
    rev_this_month = days_in_month * REVOLUTIONS_PER_DAY
    
    # points per revolution this month (visual density)
    points_per_rev = 28 + (month_idx % 3)   # 28,29,30 cycling
    
    total_points_month = int(rev_this_month * points_per_rev) + 1
    
    theta_month = np.linspace(
        current_theta,
        current_theta + rev_this_month * 2 * np.pi,
        total_points_month,
        endpoint=False
    )
    
    # Early clipping to prevent later overflow
    theta_month = np.minimum(theta_month, MAX_THETA_RAD)
    
    theta_segments.append(theta_month)
    current_theta += rev_this_month * 2 * np.pi

theta = np.concatenate(theta_segments)

# ─── Coordinates – with overflow protection ──────

r = a * np.exp(b * theta)
r = np.clip(r, 0, MAX_RADIUS)                  # prevent infinity
r = np.nan_to_num(r, nan=0.0, posinf=MAX_RADIUS, neginf=0.0)

x = r * np.cos(theta)
y = r * np.sin(theta)
z = height_per_radian * theta

# ─── Plot ────────────────────────────────────────

fig = plt.figure(figsize=(14, 11))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z,
        color='goldenrod',
        linewidth=1.1,
        alpha=0.92)

# Optional: color fades from orange → deep gold → purple
colors = plt.cm.plasma(np.linspace(0.1, 0.95, len(theta)))
ax.scatter(x, y, z, c=colors, s=1.2, alpha=0.6, edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (time · height)')

total_days = np.sum(days_per_month)
total_years_approx = total_days / 365.25

ax.set_title(
    f"Golden spiral – calendar metaphor\n"
    f"12 months • {total_days} days • ≈ {total_years_approx:.1f} years of hours\n"
    f"(28/29/30 days per month • {REVOLUTIONS_PER_DAY} rev/day • golden ratio growth)\n"
    f"Radius capped at {MAX_RADIUS} units",
    fontsize=13, pad=20
)

# Better viewing angle
ax.view_init(elev=22, azim=-58)

# Safe axis limits based on clipped values
max_r = np.max(r[np.isfinite(r)]) * 1.15 if np.any(np.isfinite(r)) else 50
ax.set_xlim(-max_r, max_r)
ax.set_ylim(-max_r, max_r)
ax.set_zlim(0, np.max(z) * 1.1)

ax.grid(True, alpha=0.12)
plt.tight_layout()

plt.show()

# Optional save (uncomment if needed)
# plt.savefig("golden_spiral_calendar_12months_fixed.png", dpi=300, bbox_inches='tight')
