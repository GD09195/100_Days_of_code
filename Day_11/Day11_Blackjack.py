from random import randint
from Day11_Blackjack_art import logo

cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10 ]

def add_card() -> int:
    return cards[randint(0,len(cards)-1)]

def calculate_score(participant_hand: list) -> int:

    score = sum(participant_hand)
    
    while score > 21 and (11 in participant_hand):
            
            participant_hand[participant_hand.index(11)] = 1
            score = sum(participant_hand)

    return score

def end_game(winner):
    
    if winner == 'player':
    
        print("You've Won! \n")

    elif winner == 'computer':     
    
        print("You've lost. \n")
    
    else:
        print("It's a Draw. \n")

    exit()

def standing():
    
    print(f"""
    ----
    Your hand: {player_hand}
    score: {player_score}

    Dealer's hand: {computer_hand}
    score: {computer_score}
    ------
    """)
    
    if player_score > 21 : end_game('computer')
    if computer_score > 21 : end_game('player')
    if computer_score < 17 or computer_score < player_score : return
    if computer_score == player_score: end_game('')
    end_game('computer')


player_hand = []
computer_hand = []

player_score = 0
computer_score = 0

player_choice = 'y'
#Initial Setup, Player 2 cards, Computer 1 card.
player_hand.append(add_card())
player_hand.append(add_card())
player_score = calculate_score(player_hand)
computer_hand.append(add_card())

computer_score = calculate_score(computer_hand)

print(logo)

#Show initial setup to the player
print(f"You: {player_hand}")
print(f"Dealer: {computer_hand}\n")

while(player_choice == 'y'):
        
    player_choice = input("Draw a card? y/n: ")

    if player_choice == 'y':
        
        player_hand.append(add_card())
        player_score = calculate_score(player_hand)
        standing()

while(True):
    computer_hand.append(add_card())
    computer_score = calculate_score(computer_hand)
    standing()

