from turtle import Turtle,Screen

import random

my_t=Turtle()
my_t.speed("fastest")
screen=Screen()
screen.colormode(255)
for i in range(100):
    colors=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    my_t.color(colors)
    my_t.circle(100)
    my_t.right(25)


screen.exitonclick()