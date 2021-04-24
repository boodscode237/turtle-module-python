import turtle as t
import random

'''
# code to extract colors from the picture
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    

print(rgb_colors)
'''

t.colormode(255)  # change color mode of turtle
tort = t.Turtle()
tort.penup()
tort.hideturtle()
tort.shape("classic")
tort.color("CadetBlue")
# make the turtle go down
tort.setheading(225)
tort.forward(300)
tort.setheading(0)
tort.speed('fastest')
number_of_dots = 100

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
              (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

for dot_count in range(1, number_of_dots + 1):
    tort.dot(20, random.choice(color_list))
    tort.forward(50)
    if dot_count % 10 == 0:
        tort.setheading(90)
        tort.forward(50)
        tort.setheading(180)
        tort.forward(500)
        tort.setheading(0)


screen = t.Screen()
screen.exitonclick()
