# Create a path using turtle graphics and render it using the Simple
# Python API.

from inkex import turtle as pturtle

# Draw the picture using inkex's turtle-graphics module.
t = pturtle.pTurtle()
t.pendown()
t.right(28)
for dist in range(500, 0, -10):
    t.forward(dist)
    t.right(121)

# Use the Simple Python API to plot the turtle's path.
path(t.getPath(), fill='none', stroke='black', stroke_width=1,
     transform='translate(600, 600)')