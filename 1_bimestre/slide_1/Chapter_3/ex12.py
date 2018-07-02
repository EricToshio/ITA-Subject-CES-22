import turtle

screen = turtle.Screen()
screen.bgcolor("#a5653a")

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("green")
bob.pensize(6)
bob.speed(1)

bob.penup()
bob.stamp()


for i in range(12):
    bob.forward(80)
    bob.pendown()
    bob.forward(10)
    bob.penup()
    bob.forward(20)
    bob.stamp()
    bob.left(180)
    bob.forward(110)
    bob.right(150)


screen.mainloop()