logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
from higherlowerdata import data

def game():
    fparty = random.choice(data)
    sparty = random.choice(data)
    if fparty==sparty:
        sparty = random.choice(data)
    print(logo)
    def repeat(fparty,sparty):
        print(f"Compare A: {fparty['name']}, {fparty['description']},from {fparty['country']}")
        print(vs)
        print(f"Against B: {sparty['name']}, {sparty['description']},from {sparty['country']}")
        choice = input("who has more folowers? Type 'A' or 'B'").lower()
        global score
        if fparty['follower_count']>sparty['follower_count']:
            if choice =='a':
                score +=1
                print(f"You're right! Your current score: {score}\n")
                fparty = random.choice(data)
                if fparty==sparty:
                   fparty = random.choice(data)
                repeat(fparty,sparty)
            else:
                print("Game over!")
                print(f"Your final score: {score}\n")
                if input("Do you want to play the game again? 'Yes' or 'No'").lower() == "yes":
                    game()
                else:
                    return()
        else:
            if choice =='b':
                score +=1
                print(f"You're right! Your current score: {score}\n")
                sparty = random.choice(data)
                if fparty==sparty:
                   sparty = random.choice(data)
                repeat(fparty,sparty)
            else:
                print("Game over!")
                print(f"Your final score: {score}\n")
                if input("Do you want to play the game again? 'Yes' or 'No'").lower() == "yes":
                    game()
                else:
                    return()
    repeat(fparty,sparty)

score = 0
game()