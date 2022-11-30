import turtle as t
from screen import SCREEN_HEIGHT
from paddle import Paddle
from screen import main_screen
from ball import Ball
import time
from score import Score

game_is_on = True
ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Score()

main_screen.onkeypress(r_paddle.go_up,"Up")
main_screen.onkeypress(r_paddle.go_down, "Down")
main_screen.onkeypress(l_paddle.go_up, "w")
main_screen.onkeypress(l_paddle.go_down, "s")

while game_is_on:
    main_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect Collision with the wall
    ball_wall_collision = ball.ycor() > (int(SCREEN_HEIGHT/2)-20) or ball.ycor() < ((int(SCREEN_HEIGHT/2*-1)+20))
   
    # Detect Collision with paddles
    ball_paddle_r_collision = ball.distance(r_paddle) < 50 and ball.xcor() > 320
    ball_paddle_l_collision = ball.distance(l_paddle) < 50 and ball.xcor() < -320
    if ball_wall_collision:
        ball.bounce_y()
    if ball_paddle_r_collision or ball_paddle_l_collision:
        ball.bounce_x()

    # Detect Right Paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

main_screen.exitonclick()