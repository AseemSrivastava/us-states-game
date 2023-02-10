import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# extract data from csv file and store it in a list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # get user input and convert it to title case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What is the name of another state?").title()
    print(answer_state)

    #Exit the program and save missing states in csv
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break

    # Check if user has guessed the correct state
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #t.write(state_data.state.item())
        t.write(answer_state)

# save data of missed states in csv files


# get mouse click coordinates
def get_mouse_click_cord(x, y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_cord)

#turtle.mainloop()

