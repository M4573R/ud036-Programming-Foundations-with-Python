import turtle

def draw_shapes():
    # get a window
    window = turtle.Screen()
    window.bgcolor("orange")

    # create turtles
    michu = turtle.Turtle()
    michu.shape("turtle")
    michu.speed(3)
    michu.color("white")

    maja = turtle.Turtle()
    maja.shape("turtle")
    maja.speed(3)
    maja.color("black")

    gucio = turtle.Turtle()
    gucio.shape("turtle")
    gucio.speed(3)
    gucio.color("green")

    # michu draws a square
    gucio.ht()
    maja.ht()
    for i in range(4):
        michu.forward(99)
        michu.right(90)

    # maja draws circle
    michu.ht()
    maja.st()
    maja.circle(99)

    # gucio draws a triangle 
    maja.ht()
    gucio.st()
    gucio.right(-70)
    for i in range(3):
        gucio.backward(99)
        gucio.right(360.0/3)
    
    gucio.ht()

    # close the window
    window.exitonclick()

draw_shapes()