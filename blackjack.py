logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random 


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards) 
#Deal the user and computer 2 cards each using deal_card() and append().

#calculate the scores
def calculate_score(owner_cards):
    score =0
    for n in range(len(owner_cards)):
        score += owner_cards[n]
    if len(owner_cards)==2 and score==21:
        score =0
    if 11 in owner_cards and score>=21:
        owner_cards.remove(11)
        owner_cards.append(1)
        calculate_score(owner_cards)
    
    return score


def compare(user_score, computer_score):
 if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
 elif user_score == computer_score:
    return "Draw 🙃"
 elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
 elif user_score == 0:
    return "Win with a Blackjack 😎"
 elif user_score > 21:
    return "You went over. You lose 😭"
 elif computer_score > 21:
    return "Opponent went over. You win 😁"
 elif user_score > computer_score:
    return "You win 😃"
 else:
    return "You lose 😤"

def game():
   user_cards = []
   computer_cards = []
   over=0
   user_cards.append(deal_card())
   computer_cards.append(deal_card())
   user_cards.append(deal_card())
   computer_cards.append(deal_card())

   while not over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
       over = 1
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
           user_cards.append(deal_card())
        else : 
           over = 1

   while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
 
   print(f"   Your final hand: {user_cards}, final score: {user_score}")
   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
   print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
   print(logo)
   game()
