import turtle
import random

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

def run_drawSpiral():
    drawSpiral(myTurtle,1000)
    myWin.exitonclick()

def tree(branchLen,t):
    if branchLen > 5:
        t.width(branchLen/10)
        t.forward(branchLen)
        angle1 = random.randrange(15,45)
        t.right(angle1)
        len1 = random.randrange(10,20)
        tree(branchLen-len1,t)
        t.left(angle1)
        angle2 = random.randrange(15,45)
        t.left(angle2)
        len2 = random.randrange(10,20)
        tree(branchLen-len2,t)
        t.right(angle2)
        t.backward(branchLen)

def draw_tree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

def main():
    draw_tree()

if __name__ == '__main__':
    main()
