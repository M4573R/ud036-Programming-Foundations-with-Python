import turtle

def draw_circle(name, distance, num_of_circles, color):
    name.color(color)
    for i in range(num_of_circles):
        for i in range(3):
            name.forward(distance)
            name.right(360.0 / 3)
        name.right(360.0 / num_of_circles)

def draw_shapes(n):
    # get a window
    window = turtle.Screen()
    window.bgcolor("orange")

    gucio = turtle.Turtle()
    gucio.shape("turtle")
    gucio.speed(0)

    # draw stick
    gucio.pensize(5)
    gucio.right(90)
    gucio.forward(200)
    gucio.backward(200)
    gucio.left(90)

    # draw flower
    gucio.pensize(1)
    draw_circle(gucio, 99, n, "white")
    draw_circle(gucio, 88, n, "blue")
    draw_circle(gucio, 77, n, "red")
    draw_circle(gucio, 66, n, "green")
    draw_circle(gucio, 55, n, "yellow")
    draw_circle(gucio, 44, n, "black")
    draw_circle(gucio, 33, n, "pink")
    draw_circle(gucio, 29, n, "#33cc8c")
    draw_circle(gucio, 26, n, "#00cc8c")
    draw_circle(gucio, 22, n, "#33aa8c")
    draw_circle(gucio, 11, n, "#33ccdd")

    gucio.ht()

    # close the window
    window.exitonclick()

draw_shapes(45)