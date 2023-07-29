#from replit import clear
#HINT: You can call clear() to clear the output in the console.

#from art import logo
#print(logo)
bid = False
dict = {}

def high(bids):
  highest = 0
  winner = ""
  for i in bids:
    if bids[i] > highest:
      highest = bids[i]
      winner = i
  print(f'Winner is {winner} with amount {highest}')

while not bid:  
  name = input("Enter name: ")
  price = int(input("Enter bid price? $"))
  dict[name] = price
  print(dict)
  ans = input("Any other person to bid? Yes or No ").lower()
  if ans == "no":
    bid = True
    high(dict)
  
    
#win = max(dict)
    
  
