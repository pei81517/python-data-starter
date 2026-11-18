import turtle

hours  = [1.0, 2.0, 2.5, 3.5, 4.0, 5.0, 6.0, 7.5]
scores = [52,  58,  63,  70,  74,  81,  88,  96]

# Compute Least Squares slope (m) and y-intercept (c)
n = len(hours)
mean_x = sum(hours) / n
mean_y = sum(scores) / n
m = sum((hours[i] - mean_x) * (scores[i] - mean_y) for i in range(n)) / sum((hours[i] - mean_x) ** 2 for i in range(n))
c = mean_y - m * mean_x

screen = turtle.Screen()
screen.title("Linear Regression Scatter Plot & Line of Best Fit")
screen.setup(width=900, height=520)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Coordinate mapping (X: 0 to 8 hrs -> -110 to 370, Y: 40% to 100% -> -140 to 160)
def get_x(h):
    return -110 + h * 60

def get_y(s):
    return -140 + (s - 40) * 5

# Draw X and Y axes
pen.pensize(2)
pen.color("black")
pen.penup()
pen.goto(-110, -140)
pen.pendown()
pen.goto(385, -140)
pen.penup()
pen.goto(-110, -140)
pen.pendown()
pen.goto(-110, 165)

# Gridlines & Y labels (50% to 100%)
pen.pensize(1)
for s in range(50, 101, 10):
    y = get_y(s)
    pen.color("lightgray")
    pen.penup()
    pen.goto(-110, y)
    pen.pendown()
    pen.goto(385, y)
    pen.color("dimgray")
    pen.penup()
    pen.goto(-150, y - 6)
    pen.write(f"{s}%", font=("Arial", 10, "normal"))

# X labels (1 to 8 hours)
pen.color("black")
for h in range(1, 9):
    x = get_x(h)
    pen.penup()
    pen.goto(x - 10, -162)
    pen.write(f"{h}h", font=("Arial", 10, "bold"))

# Draw Line of Best Fit (from x=0.5 to x=8.0)
pen.color("orangered")
pen.pensize(3)
pen.penup()
pen.goto(get_x(0.5), get_y(m * 0.5 + c))
pen.pendown()
pen.goto(get_x(8.0), get_y(m * 8.0 + c))

# Plot actual data points
for h, s in zip(hours, scores):
    x, y = get_x(h), get_y(s)
    pen.penup()
    pen.goto(x, y)
    pen.dot(10, "dodger blue")

# Plot 6.5h prediction point
pred_h = 6.5
pred_s = m * pred_h + c
pen.penup()
pen.goto(get_x(pred_h), get_y(pred_s))
pen.dot(12, "limegreen")
pen.goto(get_x(pred_h) + 8, get_y(pred_s) - 12)
pen.color("darkgreen")
pen.write(f"Prediction (6.5h → {pred_s:.1f}%)", font=("Arial", 9, "bold"))

# Title & Equation
pen.penup()
pen.color("black")
pen.goto(-110, 180)
pen.write(f"Study Hours vs. Exam Score  |  Best Fit: y = {m:.2f}x + {c:.2f}", font=("Arial", 13, "bold"))

screen.update()
screen.mainloop()