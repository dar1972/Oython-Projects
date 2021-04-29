import turtle

turtle.speed(0)

#the funtion draw the triangle which is the part of the drawing.

def triangle(t):
    turtle.pencolor("blue")
    turtle.right(30)
    turtle.forward(t)
    turtle.left(120)
    turtle.forward(t)
    turtle.left(120)
    turtle.forward(t)
    turtle.right(210)


#the set of functions makes the bowtie which includes a the circle too

def draw_one_bowtie(n):
    triangle(n)
    turtle.left(180)
    triangle(n)
    turtle.right(180)
    turtle.right(90)
    turtle.forward(n/4)
    turtle.left(90)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(n/4)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(n/4)
    turtle.right(90)
    turtle.down()

#The function makes the bowtie in recursion where it need an input for the size and the depth which is number of bows.

def draw_bowties(depth,size):
    if depth==0 or size==0:
        pass
    else:
        draw_one_bowtie(size)
        turtle.left(30)
        turtle.up()
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.left(120)
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.right(150)
        turtle.right(30)
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.right(120)
        turtle.forward(2*size)
        turtle.down()
        draw_bowties(depth-1,size/3)
        turtle.up()
        turtle.back(2*size)
        turtle.left(150)
        turtle.down()

turtle.setup(800,800)
depth = int(input("Depth = "))
draw_bowties(depth,100)

turtle.done()

