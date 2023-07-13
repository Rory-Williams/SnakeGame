from turtle import Turtle
MOVE_DIST = 20
BODY_SEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.reset()

    def reset(self):
        for seg in self.segments:  # clear existing segments
            seg.goto(1000, 1000)
        self.segments.clear()
        for idx in range(3):  # start with 3 segments
            position = idx * -BODY_SEP
            self.add_seg(position)
        self.head = self.segments[0]

    def add_seg(self, position):
        seg = Turtle(shape='square')
        seg.color('white')
        seg.pu()
        seg.goto(position, 0)
        self.segments.append(seg)

    def grow(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].setpos(x, y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
