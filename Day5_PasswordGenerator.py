import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

random_Password_Ordered = []
random_Password_scrambled = ""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(0,nr_letters):
    random_Password_Ordered.append(letters[random.randint(0, len(letters)-1)])

for i in range(0,nr_symbols):
     random_Password_Ordered.append(symbols[random.randint(0,len(symbols)-1)])

for i in range (0, nr_numbers):
    random_Password_Ordered.append(numbers[random.randint(0,len(numbers)-1)])

for char in range(0,len(random_Password_Ordered)):
    random_index = random.randint(0,len(random_Password_Ordered)-1)
    random_Password_scrambled+= random_Password_Ordered[random_index]
    random_Password_Ordered.pop(random_index)

print("Password: \n" + random_Password_scrambled)
