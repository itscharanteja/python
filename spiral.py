import turtle as t
import random
cir = t.Turtle()


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def spiral(size):
    for _ in range(int(360/size)):
        cir.speed("fastest")
        cir.color(random_color())
        cir.circle(100)
        cir.setheading(cir.heading() + size)


spiral(10)
screen = t.Screen()
screen.bgcolor("black")
screen.exitonclick()
