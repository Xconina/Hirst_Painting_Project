import turtle
import random
screen = turtle.Screen()
screen.colormode(255)

t = turtle.Turtle()
t.shape("turtle")
t.pensize(8)
t.speed(7)

def random_color():
    r= random.randint(0, 255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



direction = [0, 90, 180, 270]
for moves in range (300):
    t.color(random_color())
    t.setheading(random.choice(direction))
    t.forward(35)


screen.exitonclick()