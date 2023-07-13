from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from score_line import Line
import time

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# setup turtle objects
snake = Snake()
food = Food()
score = Score()
line = Line()
top_speed = 0.05
top_speed_seg_num = 10

# setup controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# main game loop
game_on = True
while game_on:
    snake.move()
    screen.update()

    # method to find speed based on snake length
    if len(snake.segments) < top_speed_seg_num:
        speed = top_speed + (top_speed_seg_num-len(snake.segments)) * 0.01
    else:
        speed = top_speed
    time.sleep(speed)

    # check if collision with food is made
    if snake.head.distance(food) < 10:
        print('nom')
        food.relocate()
        score.update_score()
        snake.grow()
        print(len(snake.segments))

    # check if boundaries are hit
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 220 or snake.head.ycor() < -280):
        score.reset()
        snake.reset()
        time.sleep(1)

    # check for self collision of snake
    for seg in snake.segments[1:]:
        if seg.pos() == snake.head.pos():
            score.reset()
            snake.reset()
            time.sleep(1)

screen.exitonclick()
