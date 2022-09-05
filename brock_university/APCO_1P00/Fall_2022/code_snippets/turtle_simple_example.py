import turtle       # imports the turtle graphics

t = turtle.Turtle() # creates a turtle named t
# t is centered on screen at (0, 0) pointing right
# Coordinates are given as (x, y), where
# x is the horizontal axis and y is the vertical axis
t.forward(50)       # moves 50 units, now at (50, 0)
t.right(90)         # turns 90 degrees (now facing down)
t.forward(50)       # moves 50 units, now at (50, -50)
t.right(90)         # turns 90 degrees (now facing right)
t.forward(50)       # moves 50 units, now at (0, -50)
t.right(90)         # turns 90 degrees (now facing up)
t.forward(50)       # moves 50 units, now at (0, 0)
t.right(90)         # turns 90 degrees (now facing right)
turtle.done()       # stops drawing, must be placed last!