from replit import clear
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(card):
  
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(card) == 21 and len(card)==2:
    return 0
  if sum(card) > 21 and 11 in card:
    card.remove(11)
    card.append(1)
  return sum(card)

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw "
  elif user_score == 0:
    return "Won with blackjack"
  elif computer_score == 0:
    return "Lose opponent with blackjack"
  elif user_score > 21:
    return "You lose. Opponent win!"
  elif computer_score >21:
    return "You won. Opponent lose"
  elif user_score > computer_score:
    return "You won"
  else:
    return "You lose"
def play_game():  
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Computer card is {computer_cards[0]}")
    print(f"User cards are {user_cards} and sum is {user_score}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_deal = input("Enter y to draw a new card or n to pass")
      if user_deal == "y":
        user_cards.append(deal_card())
    
      else:
        is_game_over = True
    while computer_score != 0 and computer_score <17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
    print(f"Computer cards are {computer_cards} and score {computer_score}")
    print(compare(user_score,computer_score))
while input("Want to play blackjack game y or n?: ") == "y":
  clear()
  play_game()