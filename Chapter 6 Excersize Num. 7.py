import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)

sz = 20

for i in range(5):
    sz = sz+40
    drawSquare(alex, sz)
    alex.penup()
    alex.backward(20)
    alex.right(90)
    alex.forward(20)
    alex.left(90)
    alex.pendown()


