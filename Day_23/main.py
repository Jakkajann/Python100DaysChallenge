from turtle import Turtle, Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def create_screen(screen_width, screen_height):
    created_screen = Screen()
    created_screen.setup(width=screen_width, height=screen_height)
    created_screen.tracer(0)
    return created_screen

main_screen = create_screen(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

game_is_on = True

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

main_screen.listen()
main_screen.onkeypress(player.go_up, "Up")
main_screen.onkeypress(player.go_down, "Down")

while game_is_on:
    time.sleep(0.1)
    main_screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect a sucessfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()
    


main_screen.exitonclick()

