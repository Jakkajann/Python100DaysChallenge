import pandas
import turtle
from screen import screen, image


turtle.shape(image)

data = pandas.read_csv("Day_25/50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    input_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    all_states = data.state.to_list()

    if input_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day_25/states_to_learn.csv")
        break

    if input_state in all_states:
        if input_state not in guessed_states:
            guessed_states.append(input_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == input_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(input_state)
        elif input_state in guessed_states:
            print("Already guessed state")



screen.exitonclick()