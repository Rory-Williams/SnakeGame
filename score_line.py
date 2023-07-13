from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 24, 'normal')
COLOUR = 'white'

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-300, 250)
        self.pencolor(COLOUR)
        self.pd()
        self.setheading(0)
        self.forward(600)
        self.hideturtle()
        self.pu()

