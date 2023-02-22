import turtle as t
import random

screen = t.Screen()
screen.colormode(255)
screen.bgcolor("black")
def random_color():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tom = t.Turtle()
direction = 0
tom.color("red")
tom.speed(0)
for i in range (20):
    for i in range (6):
        tom.color(random_color())
        tom.circle(80)
        direction += 3
        tom.setheading(direction)
    tom.setheading(direction + 6)
    tom.forward(200)
    tom.setheading(direction - 6)
    tom.back(400)
    # tom.setheading(direction - 6)
    tom.forward(200)
    # tom.setheading(direction + 6)
    # tom.back(200)

    
screen.exitonclick()

    # tom.setheading(direction - 6)
    # tom.forward(200)
    # tom.setheading(direction + 6)
    # tom.back(200)
