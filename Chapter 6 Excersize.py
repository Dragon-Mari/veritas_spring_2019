# 6. Use the drawsquare function we wrote in this chapter in a program to draw the image shown below. Assume each side is 20 units.
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

alex = turtle.Turtle()
for I in range(5):
    drawSquare(alex, 20)
    alex.penup()
    alex.forward(40)
    alex.pendown()
