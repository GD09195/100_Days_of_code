
import pandas as pd
import turtle


def display_state_name(state_to_display: str):
    state_row = us_states_dataframe[us_states_dataframe.state == input_state]
    state_x = state_row.x.tolist()
    state_y = state_row.y.tolist()

    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(state_x[0], state_y[0])
    new_turtle.write(state_to_display, align="Center")

def display_missed_states()-> None:
    for state in states_list:
        new_name = turtle.Turtle()
        new_name.hideturtle()
        new_name.penup()
        new_name.goto(us_states_dataframe[us_states_dataframe.state==state].x.item(), us_states_dataframe[us_states_dataframe.state==state].y.item())
        new_name.color("red")
        new_name.write(state, align="Center")

#Create dataframe from .csv
us_states_dataframe = pd.read_csv('./50_states.csv')
us_states_series = us_states_dataframe.state
states_list: list = us_states_series.to_list()

#create screen and turtle
us_states_screen = turtle.Screen()
us_states_screen.title("U.S. States Game")
image_states_path = './blank_states_img.gif'
us_states_screen.addshape(image_states_path)
turtle.shape(image_states_path)

states_guessed: int = 0
states_guessed_list: list =[]

while states_guessed < 50:
    input_state = us_states_screen.textinput(title=f'{states_guessed}/50 States Correct', prompt="Type a U.S. State ['Exit']:")
    input_state = input_state.title()

    if input_state == 'Exit':
        break

    #Check if the input_state exists in the series 'State'
    if us_states_series[us_states_series == input_state].count() >= 1:
        if input_state not in states_guessed_list:
            display_state_name(input_state)
            states_guessed += 1
            states_guessed_list.append(input_state)
            states_list.remove(input_state)


#Save states to Learn into a .csv
states_to_learn = pd.Series(data=states_list, name='States to Learn')
states_to_learn.to_csv("States_To_learn.csv")

#Display missed states
display_missed_states()



us_states_screen.exitonclick()



