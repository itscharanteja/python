# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
l_name = name.lower()

t = l_name.count("t")
r = l_name.count("r")
u = l_name.count("u")
e = l_name.count("e")
fdigit = t + r + u + e
l = l_name.count("l")
o = l_name.count("o")
v = l_name.count("v")
e = l_name.count("e")
sdigit = l + o + v + e

score = int(str(fdigit) + str(sdigit))

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


