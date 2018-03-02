import turtle
import math
screen = turtle.Screen()
screen.bgcolor("#a5653a")

bob = turtle.Turtle()
bob.hideturtle()
bob.color("green")
bob.pensize(6)

path = [(270, 100), (30,100), (120, 100), (120, 100), (225, 100*math.sqrt(2)), (225, 100), (225, 100*math.sqrt(2)), (225, 100)]

for (angle, forward) in path:
    bob.right(angle)
    bob.forward(forward)



screen.mainloop()
