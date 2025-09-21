from turtle import Turtle,Screen

t=Turtle()
s=Screen()
s.listen()

def move_forward():
    t.forward(10)
def move_backward():
    t.forward(-10)
def turn_left():
    t.left(20)
def turn_right():
    t.right(20)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.onkey(move_forward,"w")
s.onkey(move_backward,"s")
s.onkey(turn_left,"a")
s.onkey(turn_right,"d")
s.onkey(clear,"c")

s.exitonclick()
