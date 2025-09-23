from turtle import Turtle,Screen
import random

turtle_list=[]
start=False
def create_turtle():
    y_axis=120
    change=40
    for t in colors:
        new_turtle= Turtle(shape="turtle")
        new_turtle.color(t)
        new_turtle.penup()
        new_turtle.goto(-235,y_axis)
        y_axis=y_axis - change
        turtle_list.append(new_turtle)


s=Screen()
s.setup(width=500,height=400)
user_choice=s.textinput(title="Make Your bet",prompt="Which Turtle Do You Prefer?")
print(user_choice)
colors=["red","yellow","green","blue","purple","pink"]
# t.right(10)
# t.backward(100)
create_turtle()

if user_choice:
    start=True

while start:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            start=False
            if turtles.color()==user_choice:
                print(f"You won ! the Winner  Color is {turtles.color()}")
            else:
                print(f"You Lost your choice was {user_choice} the Winner Color is {turtles.color()}")

        move_forward=random.randint(0,10)
        turtles.forward(move_forward)




s.exitonclick()
