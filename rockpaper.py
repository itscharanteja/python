import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
output = [rock,paper,scissors]
user_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors.\n"))
if user_choice<0 or user_choice>=3:
    print("Invallid number")
else:
    print(output[user_choice]) 
    computer_choice = random.randint(0,2)
    print(output[computer_choice])
    print(computer_choice)
    if computer_choice == user_choice:
        print("It is a draw!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    else:
        print("Enter correct choice.")
        
