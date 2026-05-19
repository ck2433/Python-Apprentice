="""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

... # Your code here

import turtle
tina = turtle.Turtle()
tina.shape('turtle')
turtle.setup(600,600,0,0)
tina.penup()
tina.goto(100,100)
tina.pendown()
for i in range(5):
    tina.forward(150)
    tina.left(72)
turtle.exitonclick()