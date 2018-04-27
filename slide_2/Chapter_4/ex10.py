import turtle


def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

def five_star():
    t = turtle.Turtle()
    t.color("hotpink")
    t.pensize(5)
    for i in range(5):
        draw_star(t)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Draw a star")
five_star()

wn.mainloop()