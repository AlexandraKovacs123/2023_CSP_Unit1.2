
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
wall_len = 20
addition = 10
path_width = 10

# random locations
def locate()
door = rand.randint((wall_len - path_width*2), path_width * 2)
barrier = rand.randint((wall_len - path_width*2), path_width * 2)
door_length = 10

def doors():
    maze_painter.forward(door)
    maze_painter.penup()
    maze_painter.forward(door_length * 2)
    maze_painter.pendown()



def barriers():
    maze_painter.forward(barrier)
    maze_painter.left(90)
    maze_painter.forward(path_width * 2)
    maze_painter.back(path_width * 2)
    maze_painter.right(90)

def place():
    if door < barrier:
        doors()
        barriers()
    else:
        barriers()
        doors()

def spiral():
    global wall_len, addition
    maze_painter.penup()
    maze_painter.left(90)
    maze_painter.forward(20)
    maze_painter.left(90)
    maze_painter.forward(30)
    maze_painter.left(90)
    maze_painter.forward(40)
    maze_painter.pendown()
    for spiral in range(22):
        maze_painter.left(90)
        place()
        maze_painter.forward(wall_len + addition - 10 - door_length)
        addition += 10
    maze_painter.hideturtle()

spiral()

wn = trtl.Screen()
wn.mainloop()