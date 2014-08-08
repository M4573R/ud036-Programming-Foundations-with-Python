import turtle

def draw_shape():
    # get a window
    window = turtle.Screen()
    window.bgcolor("orange")

    # create a turtle called michu
    michu = turtle.Turtle()
    michu.shape("turtle")
    michu.speed(0)
    michu.color("white")


    # move michu to draw a square in the center
    michu.backward(15)

    # draw lower half
    shape = 0
    sides = 3
    while shape < 13:
        for i in range(sides):
            michu.forward(50 + sides)
            michu.right(360.0 / sides)
        sides += 1
        shape += 1
    # switch turtle
    michu.color("black")    

    # draw upper half
    shape = 0
    sides = 3
    while shape < 13:
        for i in range(sides):
            michu.forward(50 + sides)
            michu.left(360.0 / sides)
        sides += 1
        shape += 1
    
    # change connecting line color
    michu.color("orange")
    michu.forward(50)
    michu.ht()

    # close the window
    window.exitonclick()

draw_shape()