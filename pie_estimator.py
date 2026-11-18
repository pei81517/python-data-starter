import random
import math

print("--- MONTE CARLO PI ESTIMATOR ---")
total_darts = int(input("How many random darts should we throw? (e.g. 100000): "))

inside_circle = 0

for _ in range(total_darts):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Distance from center (0,0) using Pythagoras: x^2 + y^2 <= 1
    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_estimate = 4 * (inside_circle / total_darts)
error = abs(math.pi - pi_estimate)

print(f"\nDarts inside circle: {inside_circle:,} / {total_darts:,}")
print(f"Estimated Pi: {pi_estimate:.6f}")
print(f"Actual Pi:    {math.pi:.6f}")
print(f"Margin of error: {error:.6f}")