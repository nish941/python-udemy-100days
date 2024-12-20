import turtle, random

turtle.colormode(255)

sage = turtle.Turtle()
sage.shape("arrow") # circle,square,turtle,classic, triangle,arrow
screen = turtle.Screen()
sage.speed(10)
sage.pensize(7)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r,b,g)
def forwards():
    sage.pencolor(random_color())
    sage.forward(20)
def backwards():
    sage.pencolor(random_color())
    sage.backward(20)
def counter_clockwise():
    sage.left(10)
def clockwise():
    sage.right(10)
def clear():
    sage.clear()
    sage.penup()
    sage.home()  # to make it back to centre of the screen
    sage.pendown()
def circle1():
    sage.pencolor(random_color())
    sage.forward(5)
    sage.left(10)
def circle2():
    sage.pencolor(random_color())
    sage.forward(5)
    sage.right(10)
def circle3():
    sage.pencolor(random_color())
    sage.backward(5)
    sage.right(10)
def circle4():
    sage.pencolor(random_color())
    sage.backward(5)
    sage.left(10)

screen.listen()
screen.onkey(forwards,"w")
screen.onkey(backwards,"s")
screen.onkey(counter_clockwise,"a")
screen.onkey(clockwise,"d")
screen.onkey(clear,"c")
screen.onkey(circle1, "i")
screen.onkey(circle2,"j")
screen.onkey(circle3,"k")
screen.onkey(circle4,"l")

screen.exitonclick()
