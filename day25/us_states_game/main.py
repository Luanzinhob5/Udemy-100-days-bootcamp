import turtle
import pandas

FONT = ("Courier", 10, "normal")
ALIGNMENT = "center"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

def state_add(state_guess,state_x,state_y):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(int(state_x), int(state_y))
    state.write(state_guess, move=False, align=ALIGNMENT, font=FONT)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_add(answer_state, state_data.y, state_data.y)





