import turtle


def draw_star():
    t = turtle.Turtle()
    for i in range(5):
        t.forward(100)
        t.right(144)


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Draw a star")
draw_star()

wn.mainloop()