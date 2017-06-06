import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("lime")
	brad.speed(2)
	
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(25)

	window.exitonclick()

draw_square()
