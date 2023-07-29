from turtle import *
import random
t = Turtle()

color1 = ["green", "green yellow", "light green",
          "thistle", "light salmon", "wheat", "deep sky blue"]

dir = [0, 90, 180, 270]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.right(angle)
        t.forward(100)


for num_of_sides in range(3, 11):
    t.color(random.choice(color1))
    draw_shape(num_of_sides)
done()
