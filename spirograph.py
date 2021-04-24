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


tort.speed('fastest')


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tort.color(random_color())
        tort.circle(100)
        tort.setheading(tort.heading() + 10)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
