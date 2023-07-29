import turtle
import random
from turtle import Screen

turtle.colormode(255)
sc = Screen()
ar = turtle.Turtle()

color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64),
              (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170)]


ar.speed("fastest")
ar.penup()
ar.setheading(225)
ar.forward(300)
ar.setheading(0)
numofdots = 100

for dots in range(1, numofdots+1):
    ar.dot(20, random.choice(color_list))
    ar.forward(50)
    if dots % 10 == 0:
        ar.setheading(90)
        ar.forward(50)
        ar.setheading(180)
        ar.forward(500)
        ar.setheading(0)

sc.exitonclick()
