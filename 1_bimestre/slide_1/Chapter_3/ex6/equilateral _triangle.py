import turtle

screen = turtle.Screen()
screen.bgcolor("#a5653a")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("green")
bob.pensize(6)
bob.speed(1)

for _ in range(3):
    bob.forward(200)
    bob.left(120)

screen.mainloop()