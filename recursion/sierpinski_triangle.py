import turtle
import random

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

def sierpinski(degree, points, my_turtle, color):

    draw_triangle(points,color[degree],my_turtle)
    if degree > 0:
        points1 = [get_mid(points[0], points[1]), get_mid(points[0], points[2]), points[0]]
        sierpinski(degree-1,points1, my_turtle, color)
        points2 = [get_mid(points[0], points[1]), get_mid(points[1], points[2]), points[1]]
        sierpinski(degree-1,points2, my_turtle, color)
        points3 = [get_mid(points[0], points[2]), get_mid(points[1], points[2]), points[2]]
        sierpinski(degree-1,points3, my_turtle, color)

def draw_sierpinski():
    points = [[-150,-150],[150,-150],[0,150]]
    color = ['blue','red','green','white','yellow','violet','orange']
    random.shuffle(color)
    sierpinski(4, points, my_turtle, color)
    my_win.exitonclick()

def main():
    draw_sierpinski()

if __name__ == '__main__':
    main()
