from Day11_NumberGuessing_art import logo
from random import randint


def CheckGuess(current_guess):
    
    if current_guess == number:
        print(f"You guessed the number: {number} ")
        quit()

    if current_guess < number:
        print("To low")
    
    elif current_guess > number:
        print("Too high")

    return

def guess():

    print(f"You have {guesses} attempts remaining")
    guessed_number = int(input("Make a guess:"))
    
    CheckGuess(guessed_number)

    return guesses-1



number = randint(1,100)
guesses = 0
difficulty={
    "easy": 10,
    "hard": 5,
}

print(logo)
print(""""
      Welcome to the Number Guessing Game!
      I'm thinking of a number between 1 and 100.
      Try to guess it.
      """
    )

guesses = difficulty[input("Type your difficulty('easy', 'hard'): ")]

while guesses > 0:
    guesses = guess()

print(f"You lost. The number was: {number} ")


