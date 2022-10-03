import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 are correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    elif answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    else:
        print("Not a state")

missing_states = [state for state in all_states if state not in guessed_states]

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
