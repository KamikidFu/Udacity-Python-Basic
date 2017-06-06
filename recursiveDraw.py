import turtle

def draw():
    shift = 10
    total = 360
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(5)
    pen.color("yellow")

    window = turtle.Screen()
    window.bgcolor("red")

    while(total!=0):
        for i in range(4):
            pen.forward(150)
            pen.right(90)
        pen.right(shift)
        total -= shift

draw()
