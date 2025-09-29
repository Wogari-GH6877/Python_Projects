from turtle import Turtle

COLORS = ["red", "yellow", "green"]
FORWARD=20
RIGHT=180
LEFT=0
UP=90
DOWN=270

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake(3)
        self.head=self.turtle_list[0]

    def create_snake(self,num):
        j = 0

        for _ in range(num):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(0 - j, 0)
            j += 10
            self.turtle_list.append(t)

    def move(self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            # i.penup()
            x_pos = self.turtle_list[i - 1].xcor()
            y_pos = self.turtle_list[i - 1].ycor()
            self.turtle_list[i].goto(x_pos, y_pos)
        self.head.forward(FORWARD)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

