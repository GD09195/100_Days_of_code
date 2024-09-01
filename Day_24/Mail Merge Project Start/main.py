#TODO: Create a letter using starting_letter.txt 

# Open the starting_letter.txt file
with open ("./Input/Letters/starting_letter.txt") as letter_template:
    #Reading starting_letter.txt text
    letter_template_text = letter_template.read()

# Open the invited_names.txt file
with open("./Input/Names/invited_names.txt") as invited_names:
    # Reading each line in invited_names.txt in a List
    invited_names_list = invited_names.readlines()

#for each name in invited_names.txt
for name in invited_names_list:
    # Remove backspaces at the end of each name.
    name = name.strip('\n')
    # Replace the [name] placeholder with the actual name.
    new_letter_text = letter_template_text.replace("[name]", name)
    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as new_letter:
        new_letter.write(new_letter_text)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

