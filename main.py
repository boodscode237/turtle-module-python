from turtle import Turtle, Screen
import random

tort = Turtle()
tim = Turtle()

tort.shape("turtle")
colors = ['indianRed', 'gold', "orchid", "peru", 'tan', 'thistle', "salmon", "orange", "hotPink", "cyan", "aquamarine", 'coral']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tort.forward(100)
        tort.right(angle)


for shape_sides_n in range(3, 11):
    tort.color(random.choice(colors))
    draw_shape(shape_sides_n)


screen = Screen()
screen.exitonclick()
