import turtle

t = turtle.Turtle()

# Declaring the draw square function
def draw_square(size: int) -> None:
    t.pendown()
    for i in range(4):
        t.forward(size)  # changed the 50!
        t.right(90)
    t.penup()

# calling the function
draw_square(40)
t.goto(-50, 50)
draw_square(20)

turtle.done()