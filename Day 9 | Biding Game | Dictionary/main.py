# Bid Game
# Bidding Game

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
'''
print(logo)
bids = {}
bidding_finished = False

def highest(bidding_record):
    highest_bid = 0
    winner = ""
    for b in bidding_record:
        bid_amount = bidding_record[b]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = b
    print(f"The winner is {winner} with a bid of${highest_bid}")

while not bidding_finished:
    name = input("What is your name ")
    price = int(input("Whats your bid $ "))
    bids[name] = price
    a = input("Are there any other users ")
    if a == "no":
        bidding_finished = True
        highest(bids)

# ----------------------------- Future Work ----------------------

# Use clear function


