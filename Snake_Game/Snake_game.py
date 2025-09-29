from turtle import Turtle,Screen
import time
from Snake import Snake
from food import Food
from ScoreBoard import Score


s=Screen()
s.setup(width=700,height=600)
s.bgcolor("black")
s.title("My Snake Game")
snake=Snake()
food=Food()
Score=Score()

s.tracer(0)
s.listen()

num=3
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Right")
s.onkey(snake.right,"Left")

is_game_started=True
while is_game_started:
    snake.move()

    s.update()
    time.sleep(0.2)

    if snake.head.distance(food) <20:
        food.refresh_pos()
        snake.create_snake(1)
        Score.increase_score()
    if snake.head.xcor()>330 or snake.head.xcor() <-330 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        is_game_started=False
        Score.game_over()

    for segment in snake.turtle_list[1:]:
        # if snake.head == segment:
        #     pass

        if snake.head.distance(segment)< 10:
            is_game_started = False
            Score.game_over()








s.exitonclick()