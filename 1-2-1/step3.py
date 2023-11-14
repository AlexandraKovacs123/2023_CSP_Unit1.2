# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand


# -----game configuration----
shell_color = "pink"
shell_size = 2
shell_shape = "turtle"
score = 0
font_setup = ("Arial", 20, "normal")

# -----initialize turtle-----
shell = trtl.Turtle()
shell.fillcolor(shell_color)
shell.turtlesize(shell_size)
shell.shape(shell_shape)
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(400,350)
counter =  trtl.Turtle()
counter.penup()
counter.goto(-400,350)
colors = ["red", "blue", "green", "purple", "navy", "orange"]
sizes = [4,3,2,1,0.5]

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False


# -----game functions--------
def sizeChange():
    newSize = rand.choice(sizes)
    shell.turtlesize(newSize)
def colorChange():
    newColor = rand.choice(colors)
    shell.fillcolor(newColor)
    shell.stamp()
    shell.fillcolor(shell_color)
    # shell.turtlesize(shell_size)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    shell.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def update_score():
    global score  # gives this function access to the score that was created above
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def change_position():
    new_xpos = rand.randint(-300,300)
    new_ypos = rand.randint(-300,300)
    shell.penup()
    shell.hideturtle()
    shell.goto(new_xpos, new_ypos)
    shell.pendown()
    shell.showturtle()

def shell_clicked(x,y):
    countdown()
    sizeChange()
    colorChange()
    change_position()
    update_score()

#-----events----------------
shell.onclick(shell_clicked)



wn = trtl.Screen()
wn.bgcolor("light blue")
wn.ontimer(countdown, counter_interval)
wn.mainloop()
