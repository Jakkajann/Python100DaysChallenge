from turtle import Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

main_screen = Screen()

main_screen.bgcolor("black")
main_screen.setup(width=SCREEN_WIDTH, height= SCREEN_HEIGHT)
main_screen.title("My Pong Game")
main_screen.tracer(0)

main_screen.listen()