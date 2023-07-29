from turtle import Turtle, Screen

t = Turtle()

sc = Screen()

print(sc.canvheight)
t.shape("square")
t.forward(500)
t.shape("laptop")
t.right(90)
t.forward(500)
t.speed(1)
sc.exitonclick()
t.end_fill()
t.done()
