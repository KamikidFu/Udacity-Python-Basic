import turtle

def draw_shapes(shapeName, shapeSize)
        if shapeName not in ('Triangle','Circle','Square')
        print("Wrong arguments")

        window = turtle.Screen()
        window.bgcolor("red")

        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.color("lime")
        pen.speed(3)

        if shapeName == 'Triangle'
                for i in range(3)
                        pen.forward(shapeSize)
                        pen.left(60)
        elif shapeName == 'Circle'
                pen.circle(shapeSize)
        else
                for i in range(4)
                        pen.forward(shapeSize)
                        pen.right(90)

        window.exitonclick()

draw_shapes('Triangle',20)
draw_shapes('Circle',30)
draw_shapes('Square',50)
draw_shapes('Line',100)
