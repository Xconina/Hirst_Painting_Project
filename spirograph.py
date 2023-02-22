import turtle as t
import random

screen = t.Screen()
screen.colormode(255)

def random_color():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tom = t.Turtle()
direction = 0
tom.color("red")
tom.speed(15)
for i in range (120):
    tom.color(random_color())
    tom.circle(80)
    direction += 3
    tom.setheading(direction)

    
screen.exitonclick()