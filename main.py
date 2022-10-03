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

game_is_on = True
while len(guessed_states) < 50 and game_is_on:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?")

    if answer_state == "Exit":
        game_is_on = False
    elif answer_state.title() in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state.title()]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state.title())
        guessed_states.append(answer_state.title())
    else:
        print("Not a state")
