import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.shape ("square")
    brad.color("blue")
    brad.speed(4)   
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

draw_square()