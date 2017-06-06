import turtle

def draw_shapes(shapeName, shapeSize):
        if shapeName not in ('Triangle','Circle','Square'):
                print("Wrong arguments")

        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.color("lime")
        pen.speed(3)

        if shapeName == 'Triangle':
                for i in range(3):
                        pen.forward(shapeSize)
                        pen.left(120)
        elif shapeName == 'Circle':
                pen.circle(shapeSize)
        elif shapeName == 'Square':
                for i in range(4):
                        pen.forward(shapeSize)
                        pen.right(90)

def draw_things():
        window = turtle.Screen()
        window.bgcolor("red")
        
        draw_shapes('Square',50)
        draw_shapes('Circle',30)
        draw_shapes('Triangle',20)
        draw_shapes('Line',100)
        draw_shapes('Triangle',120)
        draw_shapes('Line',100)
        draw_shapes('Circle',60)
        draw_shapes('Square',20)

        window.exitonclick()
        
draw_things()
