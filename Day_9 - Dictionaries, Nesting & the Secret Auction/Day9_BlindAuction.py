import os
from Day9_BlindAuction_art import logo

def clear_screen():
    os.system("clear")
    return

participants:dict = {}
more_participants = 'y'
winner_bid = 0

while(more_participants == 'y'):

    clear_screen()
    print(logo)

    name = input("What is your name: ")
    bid_price = int(input("What's your bid:$"))
    participants[name] = bid_price
    more_participants = input("are there any other bidders? y/n: ").lower()
    
    if(bid_price > winner_bid):
        winner = name
        winner_bid = bid_price

clear_screen()
print(f"The winner is {winner} with a bid of ${participants[winner]}")
