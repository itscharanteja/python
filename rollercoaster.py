print("Welcome to Roller coaster ride!")
name = input("Enter Your Name: ")
height = int(input("Enter your height: "))
age = int(input("Enter your age: "))
fees = 0
if height > 120:
    if age <12:
        fees += 5
    elif age >=12 and age<18:
        fees +=7
    elif age >=18:
        if age >45 and age <=55:
            fees +=0
        else:
            fees +=12
    photos = input("Want photos? Y or N: ")
    if photos == "Y":
        fees +=3
    else:
        fees+=0         

print(f"Your total bill is ${fees}.")

