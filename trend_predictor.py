import math

print("--- ML LINEAR REGRESSION PREDICTOR ---")

# Dataset: Hours studied (X) vs. IGCSE Exam Score (Y)
hours  = [1.0, 2.0, 2.5, 3.5, 4.0, 5.0, 6.0, 7.5]
scores = [52,  58,  63,  70,  74,  81,  88,  96]

n = len(hours)
mean_x = sum(hours) / n
mean_y = sum(scores) / n

# Calculate slope (m) and y-intercept (c) using Least Squares
numerator = sum((hours[i] - mean_x) * (scores[i] - mean_y) for i in range(n))
denominator = sum((hours[i] - mean_x) ** 2 for i in range(n))

m = numerator / denominator
c = mean_y - m * mean_x

# Calculate Pearson correlation coefficient (r)
denom_y = sum((scores[i] - mean_y) ** 2 for i in range(n))
r = numerator / math.sqrt(denominator * denom_y)

print(f"Best-Fit Model: Score = {m:.2f} * (Hours) + {c:.2f}")
print(f"Correlation (r): {r:.4f} (1.00 = perfect positive fit)\n")

# Interactive prediction
target_hours = float(input("Enter study hours to predict exam score (e.g. 6.5): "))
predicted_score = min(100.0, m * target_hours + c)

print(f"Predicted Exam Score for {target_hours} hrs: {predicted_score:.1f}%")