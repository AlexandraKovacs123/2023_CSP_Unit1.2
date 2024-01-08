import turtle
import turtle as trtl

snake = trtl.Turtle()


wn = trtl.Screen()
wn.bgpic("snakeBg4.png")

snake.color('blue')
snake.penup()

speed = 1

def travel():
    snake.forward(speed)
    wn.ontimer(travel, 10)

wn.onkey(lambda: snake.setheading(90), 'Up')
wn.onkey(lambda: snake.setheading(180), 'Left')
wn.onkey(lambda: snake.setheading(0), 'Right')
wn.onkey(lambda: snake.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()