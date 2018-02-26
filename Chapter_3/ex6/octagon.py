import turtle

screen = turtle.Screen()
screen.bgcolor("#a5653a")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("green")
bob.pensize(6)
bob.speed(1)

for _ in range(8):
    bob.forward(100)
    bob.left(45)

screen.mainloop()