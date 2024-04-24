import os
import random
from 7day_Hangman_art import stages, logo
from 7day_Hangman_words import word_list

def clear_screen():
    os.system("clear")

def print_list(temp: list):
    print(''.join(temp))
    return

chosen_word = random.choice(word_list)
chosen_word = [char for char in chosen_word]
guessed_letters: list = ["_" for char in chosen_word]
guesses_left: int = 6

clear_screen()
print(logo)



while(guesses_left > 0) and (guessed_letters != chosen_word):

    print("Your word:")
    print_list(guessed_letters)
  
   
    guess = (input("\nGuess a letter: ")).lower()

    if guess in guessed_letters:
        clear_screen()
        print(f"\nYou already guessed this letter\n{stages[guesses_left]}")

        continue

    if guess in chosen_word:

        clear_screen()
        print(f"\nYou guessed it!\n{stages[guesses_left]}")
        for index, char in enumerate(chosen_word):
            if char == guess:
                guessed_letters[index] = char
    else: 
        guesses_left -= 1
        clear_screen()
        print(f"\nNot Found!\n{stages[guesses_left]}")

clear_screen()
if (guessed_letters == chosen_word):
    clear_screen()
    print(f"\nYou Won!\n{stages[guesses_left]}")
else:
    print("\nYou Lost!")
    print(stages[guesses_left])
    print("The word was:")
    print_list(chosen_word)
        


