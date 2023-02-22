import turtle
import random


screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("black")

#timmy turtle starting stats
timmy = turtle.Turtle()
timmy.pu()
timmy.hideturtle()
timmy.setx(-280)
y_num = -260
timmy.sety((y_num))
timmy.pensize(14)
timmy.speed(6)
color_list = [(101, 177, 219), (54, 98, 154), (191, 223, 238), (2, 18, 61), (30, 48, 126), (44, 182, 169), (197, 246, 238), (243, 200, 218), (112, 224, 247), (117, 183, 159)]
def random_color():
    choice = random.choice(color_list)
    r = choice[0]
    g = choice[1]
    b = choice[2]
    random_color = (r, g, b)
    return random_color



#move up 12 times to create new rows
for i in range (12):
    y_num += 40
    timmy.sety(y_num)
    #create 12 dots in a row (12 columns of dots)
    for _ in range (12):
        #choose a random rgb color
        timmy.color(random_color())
        timmy.dot()
        timmy.pu()
        timmy.forward(50)
    #reset x value to start
    timmy.setx(-280)
    
#exit on click
screen.exitonclick()