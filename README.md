# fibonacci_spirals_collection
a mathematical sampling of codes to visualize Fibonacci series
Golden Ratio & Fibonacci Spiral CollectionA set of Python scripts exploring golden ratio spirals, Fibonacci spirals, logarithmic spirals, and calendar-inspired variants — from simple 2D drawings to animated 3D helices.All scripts visualize the mathematical beauty of the golden ratio (φ ≈ 1.6180339887…) and the Fibonacci sequence in different ways.Current date reference: January 2026Scripts IncludedFilename / Variant
Description
Library
Style
Key Features
fibonacci_spiral_turtle.py
Classic Fibonacci squares + quarter-circle spiral
turtle
Animated 2D
Educational, draws one square at a time
fibonacci_spiral_matplotlib.py
Static Fibonacci squares (no spiral curve)
matplotlib
Static 2D plot
Clean image, easy to save/export
fibonacci_spiral_turtle_advanced.py
Labeled Fibonacci squares, fixed scale=2.5, no animation
turtle
Instant 2D
Square numbers, starts ~2 cm → large squares
pi_spiral_3d.py (early version)
Basic 3D golden spiral (logarithmic)
matplotlib 3D
Static 3D
Simple helix with golden growth
golden_spiral_360rev_12cycles.py
360 revolutions in 12 cycles with variable point density
matplotlib 3D
Static 3D
28/29/30 points per revolution
calendar_golden_spiral.py
Calendar metaphor – 12 months, 24 rev/day, color fade
matplotlib 3D
Static 3D
28/29/30 days per month, plasma color gradient
hijri_golden_spiral.py (latest)
Hijri months + day markers every ~23.75 rev + animation
matplotlib 3D
Animated 3D
Month labels, different colors per month, rotation

Requirementsbash

pip install matplotlib numpy
# turtle is included in standard Python

Quick Run Examplesbash

# Classic 2D squares + spiral
python fibonacci_spiral_turtle.py

# Static squares only
python fibonacci_spiral_matplotlib.py

# Large labeled squares (instant)
python fibonacci_spiral_turtle_advanced.py

# 3D basic golden helix
python pi_spiral_3d.py

# 360 revolutions – 12 cycles with density variation
python golden_spiral_360rev_12cycles.py

# Calendar style – 12 months, daily hours as revolutions
python calendar_golden_spiral.py

# Hijri version – month names, day markers, rotating animation
python hijri_golden_spiral.py

Mathematical BackgroundAll scripts are based on the same core idea:The golden ratio φ = (1 + √5)/2 ≈ 1.6180339887…
The Fibonacci sequence approximates φ increasingly well:Fₙ₊₁ / Fₙ → φ as n → ∞
A logarithmic spiral with growth factor φ per full turn (2π radians) has the equation:r(θ) = a · e^(bθ)
where b = ln(φ) / (2π)

This gives the characteristic self-similar property of the golden spiral.Customization TipsChange scale, a, height_per_radian to control size and stretch
Modify REVOLUTIONS_PER_DAY, days_per_month for different time metaphors
Increase MAX_THETA_RAD and MAX_RADIUS if you want longer spirals (watch for overflow)
Uncomment plt.savefig(...) lines to export high-resolution images
For animation export → uncomment ani.save(...) (requires ffmpeg installed)

LicenseMIT – free to use, modify, share, teach, present, etc.

