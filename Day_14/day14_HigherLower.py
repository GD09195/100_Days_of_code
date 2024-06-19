from Day14_HigherLower_Art import logo, vs
from day14_HigherLower_Data import data
import random
import os


def get_random_option(data_list: list) -> dict:
    return random.choice(data_list)


def compare_ab (option_a_follower: int, option_b_followers: int) -> str:
    if option_a_follower > option_b_followers:
        return 'A'
    else:
        return 'B'


def end_game(final_score: int, option_a: dict, option_b: dict) -> None:
    print(f"Sorry, that's wrong.") 
    print(f"{option_a['name']} has {option_a['follower_count']} followers.")
    print(f"{option_b['name']} has {option_b['follower_count']} followers.")
    print(f"Final Score: {final_score}")
    exit()


def display_option(option: dict, option_char: str) -> None:
    print(f"{option_char}: {option['name']} a {option['description']} from {option['country']}")


option_A = get_random_option(data)
option_B = get_random_option(data)
score = 0 

while True:

    os.system("clear")
    print(logo)
    print(f"Score: {score}")

    display_option(option_A, "A")
    print(vs)
    display_option(option_B, "B")
    
    user_answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()
    
    real_answer = compare_ab(option_A['follower_count'], option_B['follower_count'])
    
    if user_answer == real_answer:
        score += 1
    else:
        end_game(score, option_A, option_B)
    
    if real_answer == 'B':
        option_A = option_B

    option_B = get_random_option(data)