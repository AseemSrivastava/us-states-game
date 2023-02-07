import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# get user input
answer_state = screen.textinput(title="Guess the state", prompt="What is the name of another state?")
print(answer_state)

# get mouse click coordinates
def get_mouse_click_cord(x, y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_cord)

turtle.mainloop()

