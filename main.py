from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

L_POSITION = (-350, 0)
R_POSITION = (350, 0)

screen = Screen()
score = Scoreboard()
ball = Ball()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(L_POSITION)
r_paddle = Paddle(R_POSITION)

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect miss with the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect miss with the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score == 10 or score.r_score == 10:
        game_is_on = False
        score.game_over()


screen.exitonclick()
