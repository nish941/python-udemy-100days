logo = """

 /$$$$$$$$                                   /$$$$$$                                      /$$     /$$       /$$                          
|__  $$__/                                  /$$__  $$                                    | $$    | $$      |__/                          
   | $$ /$$   /$$  /$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$  | $$$$$$$  /$$ /$$$$$$$   /$$$$$$       
   | $$| $$  | $$ /$$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$| $$_  $$_  $$ /$$__  $$|_  $$_/  | $$__  $$| $$| $$__  $$ /$$__  $$      
   | $$| $$  | $$| $$  \ $$| $$$$$$$$       \____  $$| $$  \ $$| $$ \ $$ \ $$| $$$$$$$$  | $$    | $$  \ $$| $$| $$  \ $$| $$  \ $$      
   | $$| $$  | $$| $$  | $$| $$_____/       /$$  \ $$| $$  | $$| $$ | $$ | $$| $$_____/  | $$ /$$| $$  | $$| $$| $$  | $$| $$  | $$      
   | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$      |  $$$$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$  |  $$$$/| $$  | $$| $$| $$  | $$|  $$$$$$$      
   |__/ \____  $$| $$____/  \_______/       \______/  \______/ |__/ |__/ |__/ \_______/   \___/  |__/  |__/|__/|__/  |__/ \____  $$      
        /$$  | $$| $$                                                                                                     /$$  \ $$      
       |  $$$$$$/| $$                                                                                                    |  $$$$$$/      
        \______/ |__/                                                                                                     \______/       
"""

import random
num = random.randrange(0,100)

def guessing():
  print("Welcome to the guessing game!")
  print("I'm thinking of a random number within the range of 0 to 100.")
  difficulty = input("Select the difficulty of game: 'Easy' or 'Hard': ").lower()
  if difficulty == "easy":
    numchances = 10
  else :
    numchances = 5
  print(f"You have {numchances} to guess the correct number")

  while (numchances >0):
    for i in range(numchances):
      guess = int(input("Please guess a number: "))
      if guess == num:
        print(f"Congratulations! You have guessed the correct number and you still had {numchances} chances left.\n")
        return()
      elif guess<num:
        print("The number is too small")
        numchances -= 1
        print(f"You have only {numchances} chances left\n")
      else:
        print("The number is too big")
        numchances -=1
        print(f"You have only {numchances} chances left \n")
  
  if (numchances==0):
    print("You lose the game.")
    print(f"The number is {num}!\n")
    return()


loop_end = False
while( not loop_end ):
   will_continue = input("Do you want to play the number guessing game? Type 'yes or 'no'.\n")
   if will_continue == "no":
    loop_end = True
   else:
    print (logo)
    guessing()
  
