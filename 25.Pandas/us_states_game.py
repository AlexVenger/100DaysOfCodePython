import turtle
import pandas
import time

states = pandas.read_csv("50_states.csv")

guessed_states = 0
guessed_states_list = []

screen = turtle.Screen()
screen.title("U.S. Guesser")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)

turtle.shape(image)
name_writer = turtle.Turtle()
name_writer.penup()
name_writer.hideturtle()

while guessed_states < 50:
    time.sleep(0.5)
    state_guess = turtle.textinput(title=f"{guessed_states}/50 States Guessed", prompt="Type the State's name").title()
    state = states[states.state == state_guess]
    if not state.empty and state_guess not in guessed_states_list:
        name_writer.goto(state.x.iloc[0], state.y.iloc[0])
        name_writer.write(state.state.iloc[0])
        guessed_states += 1
        guessed_states_list.append(state_guess)
    elif state_guess == "Exit":
        states_to_learn = states[~states.state.isin(guessed_states_list)].state
        states_to_learn.to_csv("states_to_learn.csv")
        break

if guessed_states == 50:
    name_writer.goto(-300, 0)
    name_writer.write("Congratulations! You've guessed all 50 states!", font=("Courier", 30, "normal"))
turtle.exitonclick()
