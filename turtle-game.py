from turtle import Turtle, Screen

t = Turtle()
sc = Screen()


def move_f():
    t.forward(10)


sc.listen()
sc.onkey(key="space", fun=move_f)
sc.exitonclick()
