"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)                 # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape('turtle')
# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


tina.pencolor('Red')
tina.forward(150)
tina.left(60)
tina.pencolor('Green')
tina.forward(150)
tina.left(60)
tina.pencolor('Blue')
tina.forward(150)
tina.left(60)
tina.left(30)
tina.forward(160)
tina.left(55)
tina.forward(170)
turtle.exitonclick()
