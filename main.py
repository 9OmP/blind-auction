from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome the the Great Blind Auction !!")
game_end = False
bids = {}

# def add_bid(name, bid_amount): 
#   bids[name] = bid_amount
  
def check_bids():
  max_bid = 0
  found_key = None
  for x in bids.values():
    if max_bid < x:
      max_bid = x
  for key, value in bids.items():
    if value == max_bid:
        found_key = key
        break
  print(f"The  winner is {found_key} with a bid of {max_bid}")


while(not game_end):
  name = str(input("What is your name?: "))
  bid_amount = int(input("Enter your bid amount: "))
  bids[name] = bid_amount
  
  res = str(input("Are there any other bidders? Type 'yes or 'no': ")).lower()
  
  if res == "yes":
    clear()
  elif res == "no":
    check_bids()
    game_end = True