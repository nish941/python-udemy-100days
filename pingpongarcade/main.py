from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball 
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("Black")
screen.title("My Ping-pong Arcade")
screen.tracer(1)

player1 = Paddle(-440,0)
player2 = Paddle(440,0)

screen.listen()
screen.onkey(player1.moveup, "w")
screen.onkey(player1.movedown, "s")
screen.onkey(player2.moveup, "Up")
screen.onkey(player2.movedown, "Down")

def check_bounce(pong,choice):
    if choice == player1:
        if pong.distance(player1)<50 and pong.xcor() > -440:
            if 180< pong.heading() < 270:
                new = pong.heading() -180
                pong.setheading(-new)
                pong.move()
            elif 90< pong.heading()<180:
                new = pong.heading() -180
                pong.setheading(-new)
                pong.move()

    else:
        if pong.distance(player2)<50 and pong.xcor() < 440:
            if -90< pong.heading() <0:
                new = -pong.heading() +180
                pong.setheading(new)
                pong.move()
            elif 0< pong.heading()<90:
                new = pong.heading() -180
                pong.setheading(-new)
                pong.move()
    
pong = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    pong.move(choice)
    check_bounce(pong, choice)

screen.exitonclick()