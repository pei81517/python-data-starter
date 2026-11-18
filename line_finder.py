print("--- IGCSE STRAIGHT-LINE EQUATION SOLVER ---")

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

m = (y2 - y1) / (x2 - x1)
c = y1 - (m * x1)

print(f"\nGradient (m): {m}")
print(f"Y-intercept (c): {c}")
print(f"Line equation: y = {m}x + {c}")