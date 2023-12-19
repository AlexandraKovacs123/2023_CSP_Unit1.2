#   a123_apple_1.py
import turtle as trtl
import random as rand

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
drawer = trtl.Turtle()



letter = "a"
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)  # Make the screen aware of the new file
apple_letter_x_offset = 25
apple_letter_y_offset = 50
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

apple = trtl.Turtle()
apple.penup()
wn.tracer(False)
# -----functions-----
def draw_apple(active_apple, letter):
    active_apple.showturtle()
    active_apple.shape(apple_image)
    drawLetter(active_apple, letter)
    wn.update()

def drawLetter(active_apple, letter):
    drawer.penup()
    drawer.goto(active_apple.xcor() - apple_letter_x_offset, active_apple.ycor() - apple_letter_y_offset)
    drawer.color("white")
    drawer.clear()
    drawer.write(letter, font=("Arial", 55, "bold"))

def reset_apple(active_apple):
    global letter
    if letter_list:
        letter = rand.choice(letter_list)
        letter_list.remove(letter)
        active_apple.goto(rand.randint(-270, 270), 160)
        print(letter_list)
        draw_apple(active_apple, letter)

def draw__apple(active_box, letter):
    active_box.showturtle()
    active_box.shape(apple_image)
    drawLetter(active_box, letter)
    wn.update()



def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), apple.ycor() - 400)
    apple.hideturtle()
    wn.tracer(False)
    reset_apple(apple)

def check_A():
    global letter
    if letter == "a":
        drop_apple()

def check_B():
    global letter
    if letter == "b":
        drop_apple()

def check_C():
    global letter
    if letter == "c":
        drop_apple()

def check_D():
    global letter
    if letter == "d":
        drop_apple()

def check_E():
    global letter
    if letter == "e":
        drop_apple()

def check_F():
    global letter
    if letter == "f":
        drop_apple()


def check_G():
    global letter
    if letter == "g":
        drop_apple()


def check_H():
    global letter
    if letter == "h":
        drop_apple()

def check_I():
    global letter
    if letter == "i":
        drop_apple()

def check_J():
    global letter
    if letter == "j":
        drop_apple()


# -----function calls-----
draw_apple(apple, "A")
wn.onkeypress(check_A, "a")
draw_apple(apple, "B")
wn.onkeypress(check_B, "b")
draw_apple(apple, "C")
wn.onkeypress(check_C, "c")
draw_apple(apple, "D")
wn.onkeypress(check_D, "d")
draw_apple(apple, "E")
wn.onkeypress(check_E, "e")
draw_apple(apple, "F")
wn.onkeypress(check_F, "f")
draw_apple(apple, "G")
wn.onkeypress(check_G, "g")
draw_apple(apple, "H")
wn.onkeypress(check_H, "h")
draw_apple(apple, "I")
wn.onkeypress(check_I, "i")
draw_apple(apple, "J")
wn.onkeypress(check_J, "j")


wn.listen()
wn.bgpic("background.gif")
wn.mainloop()