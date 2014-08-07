import turtle

def draw_square():
    # get a window
    window = turtle.Screen()
    window.bgcolor("orange")

    # create a turtle called michu
    michu = turtle.Turtle()
    michu.shape("turtle")
    michu.speed(3)
    michu.color("white")

    # move michu to draw a square
    for i in range(4):
        michu.forward(99)
        michu.right(90)
    
    # close the window
    window.exitonclick()

draw_square()