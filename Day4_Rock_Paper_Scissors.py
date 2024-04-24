import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

Player_Choice = int(input("What do yo choose? \nType. \nRock: 0 \nPaper: 1 \nScissors: 2\n:"))

print(f"Player:\n {choices[Player_Choice]}")

Computer_Choice = random.randint(0,2)

print(f"Computer:\n {choices[Computer_Choice]}")

if Player_Choice == Computer_Choice:
    print("\nDraw")
elif (Player_Choice == 0 and Computer_Choice == 2) or (Player_Choice == 2 and Computer_Choice == 1) or (Player_Choice == 1 and Computer_Choice==0):
    print("\nYou win")
else: 
    print("\nYou Lose")


