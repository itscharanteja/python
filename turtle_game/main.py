from turtle import Turtle, Screen

tim = Turtle()
sc = Screen()

sc.setup(400,500)

user= sc.textinput(title='User input', prompt="Which turtle will win the race? Enter the color: ")
print(user)

sc.exitonclick()

