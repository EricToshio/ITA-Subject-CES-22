import turtle

screen = turtle.Screen()
screen.bgcolor("#a5653a")

bob = turtle.Turtle()
bob.hideturtle()
bob.color("green")
bob.pensize(6)
bob.speed(1)

for _ in range(5):
    bob.forward(100)
    bob.right(144)

screen.mainloop()