import turtle

t = turtle.Turtle()

# variables to use
num_of_shapes: int = 3
num_of_sides: int = 8
length: int = 20
space: int = 55
angle: int = 360 / num_of_sides

t.speed(10)
t.pensize(2)
t.penup()
t.goto(-85, 0)  # start further to the left

t.color("red", "yellow")
for i in range(num_of_shapes):    # outer loop
    t.pendown()
    t.begin_fill()
    for j in range(num_of_sides): # inner loop
        t.forward(length)
        t.left(angle)
    t.end_fill()
    t.penup()
    t.forward(space)

t.pendown()
# Note that we casted from a float to int
square_sides: int = int(num_of_sides / 2)
# A single loop to draw a square
for i in range(square_sides):
    t.forward(length)
    t.left(90)
t.penup()
turtle.done()