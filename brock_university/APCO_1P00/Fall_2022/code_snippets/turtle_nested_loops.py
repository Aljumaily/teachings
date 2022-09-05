import turtle

t = turtle.Turtle()
t.pensize(3)
t.color("magenta", "lavender")
for i in range(3):  # draws three squares in total
	t.pendown()
	t.begin_fill()
	for j in range(4):  # draws a single filled square
		t.forward(20)
		t.right(90)
	t.end_fill()
	t.penup()  # don't draw anything
	# forward to the same length (20) and another
	# 5 units to place a divider
	t.forward(25)
turtle.done()