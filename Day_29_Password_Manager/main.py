import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator()->None:
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_save()-> None:

    #.get entries strings
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    #save data to data.txt file
    with open('./data.txt', mode= 'a') as data_file:
        data_file.write(f'{website},{username},{password}\n')

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