import turtle

def draw_board():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

def draw_block():
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)

def draw_cube():
    turtle.fillcolor("red")
    turtle.begin_fill()
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.left(90)
    turtle.forward(10)
    draw_block()
    turtle.right(90)
    draw_block()
    turtle.end_fill()

def draw_tee():
    turtle.fillcolor("blue")
    turtle.begin_fill()
    draw_block()
    turtle.right(90)
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.left(90)
    turtle.forward(10)
    draw_block()
    turtle.end_fill()

def draw_zed():
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    draw_block()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    draw_block()
    turtle.right(180)
    turtle.forward(10)
    turtle.left(90)
    draw_block()
    turtle.right(90)
    draw_block()
    turtle.end_fill()

def draw_el():
    turtle.fillcolor("brown")
    turtle.begin_fill()
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.right(90)
    draw_block()
    turtle.end_fill()

def draw_straight():
    turtle.fillcolor("green")
    turtle.begin_fill()
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.forward(10)
    draw_block()
    turtle.end_fill()

# def was used to define a certain shape or certain group of commands so that it becomes easy the same set of commands at once and type the whole set of code the second time.

draw_board()
draw_board()

draw_cube()

turtle.left(90)
turtle.forward(10)

draw_tee()

turtle.right(90)
turtle.forward(10)
draw_zed()

turtle.right(90)
turtle.forward(10)
turtle.left(90)
draw_el()

turtle.right(180)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)

draw_tee()

turtle.right(180)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)

draw_cube()

turtle.left(90)
turtle.forward(10)
turtle.right(90)

draw_zed()

turtle.right(90)
turtle.penup()
turtle.forward(40)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.pendown()
draw_el()

turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
draw_straight()

turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(10)
turtle.right(180)
draw_straight()

turtle.done()
