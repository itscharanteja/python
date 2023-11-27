from turtle import Turtle, Screen

t = Turtle()
sc = Screen()


def move_f():
    t.forward(10)


def move_b():
    t.backward(10)


def counter_clock():
    t.left(10)


def anti_clock():
    t.right(10)


# def listen(key, func):
#     return sc.onkey(key=key, fun=func)


sc.listen()
sc.onkey(key="w", fun=move_f)
sc.onkey(key="s", fun=move_b)
sc.onkey(key="a", fun=counter_clock)
sc.onkey(key="d", fun=anti_clock)

sc.exitonclick()
