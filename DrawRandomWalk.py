from turtle import Turtle,Screen

import random
myT=Turtle()
myT.pensize(7)

colors = [
    "red", "green", "blue", "yellow", "purple", "orange", "pink",
    "brown", "black", "white", "gray", "cyan", "magenta", "gold",
    "silver", "turquoise", "violet", "indigo", "navy", "lime",
    "maroon", "olive", "teal", "coral", "salmon", "chocolate",
    "plum", "orchid", "tan", "khaki"
]
angle=[0,90,180,270,360]

for i in range(150):
    random_color=random.choice(colors)
    myT.color(random_color)
    random_direction=random.choice(angle)
    myT.forward(20)
    myT.setheading(random_direction)
screen=Screen()
screen.exitonclick()

