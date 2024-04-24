import os
from Day8_art import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(message: str, shift: int, mode: str) -> str :

    message_encrypted = [char for char in message]
    alphabet_lenght = len(alphabet)-1

    if shift > len(alphabet): shift = shift%len(alphabet)
   
    if mode == 'decode':
        shift *= (-1)

    for index, char in enumerate(message_encrypted):
        
        if char not in alphabet: continue 

        alphabet_index = alphabet.index(char)

        if(alphabet_index + shift > alphabet_lenght):

          alphabet_index = shift - (alphabet_lenght-alphabet_index) - 1
           
        else:
            alphabet_index = alphabet_index + shift 

        message_encrypted[index] = alphabet[alphabet_index]
    
    return ''.join(message_encrypted)

os.system("clear")
print(logo)
repeat = "yes"

while(repeat == 'yes'):

    action = input("Type 'Encode' to encrypt, type 'Decode' to decrypt: \n").lower()
    message = input("Type your message: \n").lower()
    shift = int(input ("Type your shift number:\n"))
    print(f"Your Message:\n{caesar(message, shift, action)}")

    repeat = input("Type 'yes' if you wan to go again. Otherwise type 'no':\n")

print ("\nGoodbye")

