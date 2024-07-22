# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# #TODO-1: Import and print the logo from art.py when the program starts.
# '''from art import logo
# print(logo)'''

# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   #Try running the program and entering a shift number of 45.
#   #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#   #Hint: Think about how you can use the modulus (%).
#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")

# for i in range(10):
#
#     print(i*i)

# def twosum(nums):
#     leng = len(nums)
#     for i in range(0,leng):
#         print(i)
#         for j in range(2,leng):
#             print(j)


# print(twosum([2,3,4,5]))


import tkinter as tk
import time

def move_disks(n, source, auxiliary, target):
    # Base case: if the number of disks is 0, do nothing
    if n == 0:
        return
    
    # Step 1: Move n-1 disks from source to auxiliary
    move_disks(n - 1, source, target, auxiliary)
    
    # Step 2: Move the largest disk from source to target
    paint_disks(source, aux)
    tk.update()
    time.sleep(1)
    paint_disks(target, source)
    tk.update()

    # Step 3: Move n-1 disks moved earlier to target
    move_disks(n - 1, auxiliary, source, target)

def paint_disks(pole1, pole2):
    disks = [disks[i] for i in range(len(disks)) if disks[i]["h"] > pole1.get()]
    if len(disks) > 0:
        for disk in disks:
            canvas.delete(disk["id"])
    disks = [disks[i] for i in range(len(disks)) if disks[i]["h"] > pole2.get()]
    for disk in disks:
            disk_id = canvas.create_rectangle(pole2.get() - 10, disk["h"] - disk["h"] / 3, pole2.get() + 10, disk["h"] + disk["h"] / 3, outline="black", fill="white")
            disk["id"] = disk_id
            disks[i]["id"] = disk_id

def start_game():
    play = input("Press 'y' to play the game: ").lower()
    if play == 'y':
        move_disks(3, "A", "B", "C")

# Define the canvas
canvas = tk.Canvas(width=700, height=500)
canvas.grid(row=0, column=0)
xa, ya, xb, yb, xc, yc = 100, 100, 100, 200, 100, 300

# Define the disks
disks = [[100, 100, 30], [115, 150, 15], [130, 200, 10]]

# Define the buttons
tk.Button(text="Start", command=start_game).grid(row=2, column=0)
tk.Button(text="Step", command=lambda: move_disks(3, "A", "B", "C")).grid(row=2, column=1)

tk.mainloop()

canvas.pack()
canvas.create_line(xa, ya, xb, ya, xc, xc, xa, ya)
canvas.create_line(xb, yb, xc, yc, xa, yc)
canvas.create_line(xa, ya, xa, yc)
canvas.create_line(xb, yb, xb, yc)
canvas.create_line(xc, yc, xc, ya)

# Fill each pole's canvas portions with disk's white color
canvas.create_rectangle(xa, ya, xa + 25, ya + 25, outline="black", fill="white")
canvas.create_rectangle(xb, yb, xb + 25, yb + 25, outline="black", fill="white")
canvas.create_rectangle(xc, yc, xc + 25, yc + 25, outline="black", fill="white")