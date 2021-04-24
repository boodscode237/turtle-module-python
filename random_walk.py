from turtle import Turtle, Screen
import random

tort = Turtle()

tort.shape("turtle")
colors = ['indianRed', 'gold', "orchid", "peru", 'tan', 'thistle',
          "salmon", "orange", "hotPink", "cyan", "aquamarine", 'coral']
directions = [0, 90, 180, 270]
tort.pensize(15)
# tort.speed('fastest')

for _ in range(1_000_000_000_000_000_000_000_000_000_000_000):
    tort.color(random.choice(colors))
    tort.forward(30)
    tort.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
