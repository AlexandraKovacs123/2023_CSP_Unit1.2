import turtle as trtl
import random as rand


#creating turtles
apple_image = "apple5.gif"
apple = trtl.Turtle()
snake = trtl.Turtle()
scores = trtl.Turtle()
wn = trtl.Screen()
#set up snake and turtle
wn.addshape(apple_image)
apple.shape(apple_image)
apple.hideturtle()
apple.penup()
apple.goto(50,0)
apple.showturtle()
wn.bgcolor("black")
snake.color('red')
snake.penup()
speed = .3
def travel():
   snake.forward(speed)
   wn.ontimer(travel, 1)
   touch()

wn.onkey(lambda: snake.setheading(90), 'Up')
wn.onkey(lambda: snake.setheading(180), 'Left')
wn.onkey(lambda: snake.setheading(0), 'Right')
wn.onkey(lambda: snake.setheading(270), 'Down')


def randomapple():
   apple.penup()
   possible = [-175, -125, -75, -25, 25, 75, 125, 175]
   locationx = rand.choice(possible)
   locationy = rand.choice(possible)
   apple.hideturtle()
   apple.goto(locationx, locationy)
   apple.showturtle()
def touch():
    score = ""
    if abs(apple.xcor() - snake.xcor()) < 7:
       if abs(apple.ycor() - snake.ycor()) < 7:
           global speed
           print("good")
           randomapple()
           speed += .1
           score += 1
           scores.write(score)




wn.listen()
travel()
randomapple()
wn = trtl.Screen()
wn.bgpic("snakeBg4.png")
wn.mainloop()
