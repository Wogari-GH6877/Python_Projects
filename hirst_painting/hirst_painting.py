import colorgram
from turtle import Turtle, Screen
import random



# rgb_color=[]
# colors = colorgram.extract('color_img.jpg', 25)
#
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r,g,b))
#
# print(rgb_color)

my_t = Turtle()
screen = Screen()
screen.colormode(255)
my_t.setheading(225)
my_t.hideturtle()
my_t.up()
my_t.forward(250)
my_t.setheading(0)
def random_painting():
    for i in range(10):
        for j in range(10):
            current_color = color_list[random.randint(0, len(color_list) - 1)]
            my_t.dot(20, current_color)
            my_t.penup()
            my_t.forward(30)
            my_t.pendown()
        my_t.setheading(90)
        my_t.dot(20, current_color)
        my_t.penup()
        my_t.forward(30)
        if i%2==0:
            my_t.left(90)
        else:
            my_t.right(90)



color_list=[(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9)]

random_painting()

screen.exitonclick()

