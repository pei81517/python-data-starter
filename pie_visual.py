import turtle
import random

# Set up the drawing window
screen = turtle.Screen()
screen.title("Visual Monte Carlo Pi Simulator")
screen.setup(width=600, height=600)
screen.tracer(0)  # Makes drawing super fast

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Draw the 400x400 square boundary (-200 to 200)
pen.penup()
pen.goto(-200, -200)
pen.pendown()
pen.pensize(2)
for _ in range(4):
    pen.forward(400)
    pen.left(90)

# Draw the inscribed circle (radius 200)
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.circle(200)

# Throw 2,000 visual darts
total_darts = 2000
inside_circle = 0

for i in range(1, total_darts + 1):
    x = random.uniform(-200, 200)
    y = random.uniform(-200, 200)

    pen.penup()
    pen.goto(x, y)

    if x**2 + y**2 <= 200**2:
        inside_circle += 1
        pen.dot(4, "dodger blue")  # Inside circle
    else:
        pen.dot(4, "tomato")       # Outside circle

    if i % 50 == 0:
        screen.update()

pi_estimate = 4 * (inside_circle / total_darts)
print(f"Visual Darts Thrown: {total_darts}")
print(f"Estimated Pi: {pi_estimate:.4f}")

screen.update()
screen.mainloop()