import turtle
def draw():
    shift = 5
    total = 360
    window = turtle.Screen()
    window.bgcolor("red")

    pen = turtle.Turtle()
    pen.speed(50)
    pen.color("yellow")
    while(total!=0):
        for i in range(4):
            if(i%2==0):
                pen.forward(50)
                pen.right(30)
            else:
                pen.forward(50)
                pen.right(150)
        pen.right(shift)
        total -= shift

    pen.right(90)
    pen.forward(200)

    window.exitonclick()
draw()
    
