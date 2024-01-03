
import turtle as trtl
import random as rand

maze_painter = trtl.Turtle()
'''
x = starting distance
y = incremental distance

In a loop:
    1. go forward x
    2. turn left 90 degrees
    3. go forward x + y
    4. turn left 90 degrees
'''
'''
barriers:

in the door function
after drawing door
1. forward 40
2. turn right 90
3. forward path width
4. turn right 180
5. forward path width
6. turn right 90
7. continue walls
'''

maze_painter.pensize(3)
path_width = 15
wall_len = path_width


def spiral():
    global wall_len
    for w in range(26):
        wall_len += path_width

        if (w > 4):
            randomNum = rand.randint(0, 1)

            # Initial turn for painter to be in the correct direction
            maze_painter.left(90)

            if randomNum == 1:
                # Draw the door
                doors()
                # Draw the barrier
                barriers()

            else:
                # Draw the barrier
                barriers()
                # Draw the door
                doors()

            # Remember: you have to subtract the amount you drew for the wall and
            # barrier to avoid making the walls bigger.
            maze_painter.forward(wall_len - 10 - path_width - 40)


def doors():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()


def barriers():
    # draw barrier wall
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.backward(path_width * 2)
    maze_painter.right(90)


spiral()

maze_painter.hideturtle()


wn = trtl.Screen()
wn.mainloop()
