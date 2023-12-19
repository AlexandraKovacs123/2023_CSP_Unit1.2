
import turtle as trtl

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
original = 10
addition = 10
maze_painter.left(90)
maze_painter.forward(original)

for spiral in range(24):
    maze_painter.left(90)
    maze_painter.forward(original + addition)
    addition += 10

def doors():
    path_width = 10
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()


wn = trtl.Screen()
wn.mainloop()