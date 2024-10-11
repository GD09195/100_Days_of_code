import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator()->None:

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for i in range(randint(8,10))]
    random_symbols = [choice(symbols) for i in range(randint(2,4))]
    random_numbers = [choice(numbers) for i in range(randint(2,4))]

    random_password = random_letters+random_symbols+random_numbers

    shuffle(random_password)

    random_password_str: str = ''.join(random_password)

    entry_password.delete(0, tkinter.END)
    entry_password.insert(0,random_password_str)

    pyperclip.copy(text= random_password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_save()-> None:

    #.get entries strings
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    new_data: dict = {
        website: {
            'username': username ,
            'password': password,
            },
        }

    if website == '' or password == '' or website== '':
        messagebox.showwarning(title= 'Oops', message= "Please don't leave any fields empty!")
        return

    #Message Box
    #ok_to_save = messagebox.askokcancel(title= website, message= f'Save the following?\nUsername:{username}\nPassword:{password}')

    #save Data into a txt
    #with open('./data.txt', mode= 'a') as data_file:
        #data_file.write(f'{website},{username},{password}\n')

    #write data to a json file
    with open('./data.json', mode= 'w') as data_file:
        json.dump(new_data, data_file, indent= 4)

    #Read data from a json file
    #with open('./data.json', mode='r') as data_file:
        #data_dict = json.load(data_file)

    #Clear the Website & Password Entries
    entry_website.delete(0, tkinter.END)
    entry_password.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #

#Welcome Window
window_welcome = tkinter.Tk()
window_welcome.title('Password Manager')
window_welcome.config(padx=40, pady=40)

#Canvas on Welcome Window
canvas_mypass = tkinter.Canvas(width=200, height=200, highlightthickness=0)
image_mypass = tkinter.PhotoImage(file='./logo.png')
canvas_mypass.create_image(100,100, image=image_mypass)
canvas_mypass.grid(row= 0, column= 1)

#Labels
#website
label_website = tkinter.Label(text="Website:", font=("Arial", 10))
label_website.grid(row= 1, column= 0)
#Email/Username:
label_username = tkinter.Label(text="Email/Username:", font=("Arial", 10))
label_username.grid(row= 2, column= 0)
#Password
label_password = tkinter.Label(text="Password:", font=("Arial", 10))
label_password.grid(row= 3, column= 0)

#Entries

#Website
entry_website = tkinter.Entry(width= 40)
entry_website.grid(row= 1, column= 1, columnspan= 2)
entry_website.focus()
#Email/Username
entry_username = tkinter.Entry(width=40)
entry_username.grid(row= 2, column= 1, columnspan= 2)
entry_username.insert(tkinter.END,'gd091295@gmail.com')
#Password
entry_password = tkinter.Entry(width= 20)
entry_password.grid(row= 3, column= 1)

#Buttons

#Generate Password
button_generate_Password = tkinter.Button(text= 'Generate Password', command= pass_generator)
button_generate_Password.grid(row= 3, column= 2)
#Add
button_add = tkinter.Button(text= 'Add', width= 36, command= pass_save)
button_add.grid(row= 4, column= 1, columnspan=2)



window_welcome.mainloop()