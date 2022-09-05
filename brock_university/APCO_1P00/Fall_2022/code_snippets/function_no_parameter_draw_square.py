import turtle
t = turtle.Turtle()

# Declaring the draw square function
def draw_square() -> None:
    t.pendown()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.penup()

# calling the function
draw_square()
t.goto(100, 100)
draw_square()

turtle.done()