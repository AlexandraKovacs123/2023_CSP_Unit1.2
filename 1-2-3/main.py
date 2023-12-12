#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_an_A():
  apple.color("white")
  apple.write("A", font=("Arial", 25, "bold"))


def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  draw_an_A()

def move():
  apple.xcor()
  apple.ycor()
  apple.penup()
  apple.goto(0,-160)

def drop():
  move()




#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop, "a")

wn.listen()

wn.mainloop()