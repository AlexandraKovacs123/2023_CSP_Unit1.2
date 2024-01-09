# import turtle & random
import turtle as trtl
import random as rand

# Create turtles & images
snake = trtl.Turtle()
apples = "apple5.gif"
apple = trtl.Turtle()
wn = trtl.Screen()
wn.bgpic("snakeBg4.png")
wn.addshape(apples)

snake.color('blue')
snake.penup()
apple.shape(apples)
snake.turtlesize(2)
speed = 1


# turtle movement
def travel():
    snake.forward(speed)
    wn.ontimer(travel, 10)


wn.onkey(lambda: snake.setheading(90), 'Up')
wn.onkey(lambda: snake.setheading(180), 'Left')
wn.onkey(lambda: snake.setheading(0), 'Right')
wn.onkey(lambda: snake.setheading(270), 'Down')


def randLocate():
    possible = [-175, -125, -75, -25, 25, 75, 125, 175]
    locationX = rand.choice(possible)
    locationY = rand.choice(possible)
    apple.penup()
    apple.hideturtle()
    apple.goto(locationX, locationY)
    apple.showturtle()

wn.listen()

travel()
randLocate()

wn.mainloop()