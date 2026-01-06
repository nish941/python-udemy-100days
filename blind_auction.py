logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                      
                YOU'RE WELCOME TO BLIND AUCTION !!
'''
print(logo)
bids = {}
bid_end = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_end:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  willcontinue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if willcontinue == "no":
    bid_end = True
    find_highest_bidder(bids)
 