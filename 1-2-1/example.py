import turtle as trtl

test = trtl.Turtle()

def drawTriangle(long, x, y):
    test.penup()
    test.goto(x, y)
    test.pendown()
    test.forward(long)
    test.right(120)
    test.forward(long)
    test.right(120)
    test.forward(long)

x = 100
y = 100
length = 43
for tri in range(100):
    drawTriangle(length, x, y)
    x += length * 1.25
    y += length * 1.25
    length += 1

wn = trtl.Screen()
wn.mainloop()