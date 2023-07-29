from random import randint

easy = 10
hard = 5
 
num = randint(0,100)

def diff():
    user_diff = input("Want to play easy or hard?: ").lower()
    if user_diff == "easy":
        
        print("You have 10 chances to guess.")
        return easy
    elif user_diff == "hard":
        
        print("You have 5 chances to guess.")
        return hard
    else:
        print("Choose the correct one.")
        
def game():
    print("Welcome to Number guessing game. ")
    print("Choose your difficulty. ")
    chance = diff()
    while chance > 0:
        guess = int(input("Give it a go! Guess a number. "))
        print(f"You left with {chance} chances")
        if guess > num:
            print("Too high ")
            chance -= 1
        elif guess < num:
            print("Too low")
            chance -=1
        else:
            print(f"You guessed right, You won! Guessed num is {num}")
            return
        if chance == 0:
            print(f"You lost! The number is {num}")
            return    
game()
