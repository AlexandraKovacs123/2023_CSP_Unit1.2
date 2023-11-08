# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand


# -----game configuration----
shell_color = "pink"
shell_size = 2
shell_shape = "turtle"
score = 0

# -----initialize turtle-----
shell = trtl.Turtle()
shell.fillcolor(shell_color)
shell.turtlesize(shell_size)
shell.shape(shell_shape)
# -----game functions--------
def change_position():
    new_xpos = rand.randint(-300,300)
    new_ypos = rand.randint(-300,300)
    shell.penup()
    shell.hideturtle()
    shell.goto(new_xpos, new_ypos)
    shell.pendown()
    shell.showturtle()

def shell_clicked(x,y):
    change_position()

#-----events----------------
shell.onclick(shell_clicked)


wn = trtl.Screen()
wn.mainloop()
