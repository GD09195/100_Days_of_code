from Day14_HigherLower_Art import logo, vs
from day14_HigherLower_Data import data
import random
import os

def get_random_option(Data_List : list) -> dict:
    return random.choice(Data_List)

def compare_AB (optionA_Follower: int, optionB_Followers: int) -> str :
    
    if optionA_Follower > optionB_Followers:
        return 'A'
    else:
        return 'B'

def endGame(finalscore: int, optionA : dict, optionB: dict)-> None:
    print(f"Sorry, that's wrong.") 
    print(f"{optionA['name']} has {optionA['follower_count']} followers.")
    print(f"{optionB['name']} has {optionB['follower_count']} followers.")      
    print(f"Final Score: {finalscore}")
    exit()

def display_option(option: dict, optionChar: str)->None:
        print(f"{optionChar}: {option['name']} a {option['description']} from {option['country']}")

option_A = get_random_option(data)
option_B = get_random_option(data)
score = 0 

while(True):

    os.system("clear")
    print(logo)
    print(f"Score: {score}")

    display_option(option_A, "A")
    print(vs)
    display_option(option_B, "B")
    
    user_answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()
    
    real_answer = compare_AB(option_A['follower_count'], option_B['follower_count'])
    
    if user_answer == real_answer:
        score+=1
    else:
        endGame(score, option_A, option_B)
    
    if(real_answer == 'B'):
        option_A = option_B

    option_B = get_random_option(data)