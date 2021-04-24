import turtle as t
import random

tort = t.Turtle()
t.colormode(255)

tort.shape("turtle")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_colour = (red, green, blue)
    return random_colour


directions = [0, 90, 180, 270]
tort.pensize(15)
tort.speed('fastest')

for _ in range(1_000):
    tort.color(random_color())
    tort.forward(30)
    tort.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
