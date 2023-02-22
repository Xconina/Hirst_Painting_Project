import turtle
from random import randint
screen = turtle.Screen()
screen.colormode(255)

tommy = turtle.Turtle()
tommy.pu()

tommy.shape("turtle")

tommy.setx(-15)

tommy.sety(100)
tommy.pensize(2.5)
tommy.pd()




num_sides = 3
for times in range (7):
    tommy.color(randint(0,255),
                randint(0,255),
                randint(0,255))
    for _ in range(num_sides):
        angle = 360/ num_sides
        tommy.forward(100)
        tommy.right(angle)
    num_sides += 1
screen.exitonclick()
