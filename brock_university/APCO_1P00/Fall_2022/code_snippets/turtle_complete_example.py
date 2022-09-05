import turtle

t = turtle.Turtle()
turtle.title("Example!")    # sets the window title
turtle.bgcolor("bisque")    # set the background colour
print(t.pensize())          # prints 1
t.pensize(3)                # now the pen is thicker
print(t.speed())            # prints 3
t.speed(0)                  # super fast!
t.pencolor("blue")
t.fillcolor("maroon1")
# Instead of the two lines above, use the shortcut
# t.color("blueviolet", "green2")
t.hideturtle()              # turtle not visible any more
t.begin_fill()              # ensures to fill the shape
t.forward(50)
print(t.pos())              # prints (50.00,0.00)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()                # stops shape filling
t.penup()                   # nothing will be drawn
# Moving to a different location
t.setx(-25)
t.sety(50)
# Instead of the two lines above, use the shortcut
# t.goto(50, 50)
t.color("green", "gold")    # changing the colours
t.pendown()                 # starts drawing again
t.begin_fill()
t.forward(25)
t.left(120)
t.forward(25)
t.left(120)
t.forward(25)
t.left(120)
t.end_fill()
t.showturtle()              # turtle is visible

turtle.done()               # keeps the output visible