"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(999999999)                           # Make the turtle move as fast, but not too fast. 

for i in range(229):
    tina.forward(150)                      # Move tina forward by the forward distance
    tina.left(65)  
    tina.penup()
    tina.goto(50,50)
    tina.pendown()
    for a in range(229):
        tina.forward(40)
        tina.left(65)                        # Turn tina left by the left turn
 # Continue the last two steps three more times   # to draw a square


turtle.exitonclick()                    # Close the window when we click on it