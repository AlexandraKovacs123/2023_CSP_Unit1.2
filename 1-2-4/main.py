
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

wall_len = 10
addition = 10
maze_painter.penup()
maze_painter.left(90)
maze_painter.forward(20)
maze_painter.left(90)
maze_painter.forward(30)
maze_painter.left(90)
maze_painter.forward(40)
path_width = 10

# random locations
door = rand.randint(path_width * 2, (wall_len - ))

def doors():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()
    barriers()


def barriers():
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.back(path_width * 2)
    maze_painter.right(90)



for spiral in range(22):
    maze_painter.pendown()
    maze_painter.left(90)
    doors()
    maze_painter.forward(original + addition)
    addition += 10



wn = trtl.Screen()
wn.mainloop()