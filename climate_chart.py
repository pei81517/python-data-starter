import csv
import turtle

months, auckland, shenzhen = [], [], []
with open("climate_data.csv", "r") as file:
    for row in csv.DictReader(file):
        months.append(row["Month"])
        auckland.append(float(row["Auckland_C"]))
        shenzhen.append(float(row["Shenzhen_C"]))

screen = turtle.Screen()
screen.title("Auckland vs. Shenzhen Monthly Temperature (°C)")
screen.setup(width=900, height=520)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def get_x(index):
    return -110 + index * 48

def get_y(temp):
    return -140 + temp * 8.5

# Axes
pen.pensize(2)
pen.color("black")
pen.penup()
pen.goto(-130, -140)
pen.pendown()
pen.goto(435, -140)
pen.penup()
pen.goto(-130, -140)
pen.pendown()
pen.goto(-130, 165)

# Gridlines
pen.pensize(1)
for t in [10, 20, 30]:
    y = get_y(t)
    pen.color("lightgray")
    pen.penup()
    pen.goto(-130, y)
    pen.pendown()
    pen.goto(435, y)
    pen.color("dimgray")
    pen.penup()
    pen.goto(-172, y - 6)
    pen.write(f"{t}°C", font=("Arial", 10, "normal"))

# Month labels
pen.color("black")
for i, m in enumerate(months):
    pen.penup()
    pen.goto(get_x(i) - 10, -162)
    pen.write(m, font=("Arial", 10, "bold"))

def plot_curve(temps, color, label_offset):
    pen.color(color)
    pen.pensize(3)
    for i, temp in enumerate(temps):
        x, y = get_x(i), get_y(temp)
        pen.penup() if i == 0 else None
        pen.goto(x, y)
        pen.pendown()
        pen.dot(8, color)
        pen.penup()
        pen.goto(x - 10, y + label_offset)
        pen.write(f"{temp}", font=("Arial", 9, "normal"))
        pen.goto(x, y)
        pen.pendown()

plot_curve(auckland, "dodger blue", -16)
plot_curve(shenzhen, "orangered", 8)

# Title & Legend
pen.penup()
pen.color("black")
pen.goto(-130, 180)
pen.write("Auckland vs. Shenzhen Monthly Temperatures (°C)", font=("Arial", 14, "bold"))
pen.goto(250, 180)
pen.color("dodger blue")
pen.write("● Auckland", font=("Arial", 11, "bold"))
pen.goto(345, 180)
pen.color("orangered")
pen.write("● Shenzhen", font=("Arial", 11, "bold"))

screen.update()
screen.mainloop()