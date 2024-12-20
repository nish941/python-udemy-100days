from turtle import Turtle
import random

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed(10)
        self.setheading(90)
        self.hideturtle()
        self.goto(x,y)
        self.showturtle()
    
    def moveup(self):
        self.setheading(90)
        if (self.ycor()<240):
            self.forward(40)

    def movedown(self):
        self.setheading(90)
        if(self.ycor()>-240):
            self.backward(40)


class Ball(Turtle):
  
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(10)

    def move(self):
        self.setheading(random.randint(0,360))
        self.forward(5)
        if 0< self.xcor()< 460:
            angle = self.setheading(random.randint(100,260))
            if -280<self.ycor()<280:
              self.forward(5)
            elif self.ycor()>=280:
                new = self.setheading(angle) + 90
                self.setheading(new)
                self.forward(5)
            else:
                new = 360 -self.setheading(angle)
                self.setheading(new)
                self.forward(5)
        else:
            angle = self.setheading(random.randint(-80,80))
            if -280<self.ycor()<280: 
              self.forward(5)
            else:
                new = 0 - angle
                self.setheading(new)
                self.forward(5)
    
    

    # we need to detect wall collision and make it bounce back 
    # only on top and bottom, sides should be covered by the paddle
