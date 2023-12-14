#   a123_apple_1.py
import turtle as trtl
import random as rand

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
drawer = trtl.Turtle()

wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)  # Make the screen aware of the new file
apple_letter_x_offset = 25
apple_letter_y_offset = 50
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

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
    if letter_list:
        letter = rand.choice(letter_list)
        letter_list.remove(letter)
        active_apple.goto(rand.randint(-270, 270), 160)
        print(letter_list)
        draw_apple(active_apple, letter)

def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), apple.ycor() - 400)
    apple.hideturtle()
    wn.tracer(False)
    reset_apple(apple)

def check_A():
    if

# -----function calls-----
draw_apple(apple, "A")
wn.onkeypress(drop_apple, "a")
draw_apple(apple, "B")
wn.onkeypress(drop_apple, "b")
draw_apple(apple, "C")
wn.onkeypress(drop_apple, "c")
draw_apple(apple, "D")
wn.onkeypress(drop_apple, "d")
draw_apple(apple, "E")
wn.onkeypress(drop_apple, "e")
draw_apple(apple, "F")
wn.onkeypress(drop_apple, "f")
draw_apple(apple, "G")
wn.onkeypress(drop_apple, "g")
draw_apple(apple, "H")
wn.onkeypress(drop_apple, "h")
draw_apple(apple, "I")
wn.onkeypress(drop_apple, "i")
draw_apple(apple, "J")
wn.onkeypress(drop_apple, "j")
draw_apple(apple, "K")
wn.onkeypress(drop_apple, "k")
draw_apple(apple, "L")
wn.onkeypress(drop_apple, "l")
draw_apple(apple, "M")
wn.onkeypress(drop_apple, "m")
draw_apple(apple, "N")
wn.onkeypress(drop_apple, "n")
draw_apple(apple, "O")
wn.onkeypress(drop_apple, "o")
draw_apple(apple, "P")
wn.onkeypress(drop_apple, "p")
draw_apple(apple, "Q")
wn.onkeypress(drop_apple, "q")
draw_apple(apple, "R")
wn.onkeypress(drop_apple, "r")
draw_apple(apple, "S")
wn.onkeypress(drop_apple, "s")
draw_apple(apple, "T")
wn.onkeypress(drop_apple, "t")
draw_apple(apple, "U")
wn.onkeypress(drop_apple, "u")
draw_apple(apple, "V")
wn.onkeypress(drop_apple, "v")
draw_apple(apple, "W")
wn.onkeypress(drop_apple, "w")
draw_apple(apple, "X")
wn.onkeypress(drop_apple, "x")
draw_apple(apple, "Y")
wn.onkeypress(drop_apple, "y")
draw_apple(apple, "Z")
wn.onkeypress(drop_apple, "z")


wn.listen()
wn.bgpic("background.gif")
wn.mainloop()