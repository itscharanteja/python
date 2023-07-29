import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
# color1 = ["green", "green yellow", "light green",
#           "thistle", "light salmon", "wheat", "deep sky blue"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


dir = [0, 90, 180, 270]


for _ in range(200):
    tim.pensize(10)
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(dir))


done()
