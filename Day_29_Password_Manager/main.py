import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

#Welcome Window
window_welcome = tkinter.Tk()
window_welcome.title = 'Password Manager'
window_welcome.config(padx=20, pady=20)

#Canvas on Welcome Window
canvas_mypass = tkinter.Canvas(width=200, height=200, highlightthickness=0)
image_mypass = tkinter.PhotoImage(file='./logo.png')
canvas_mypass.create_image(200,200, image_mypass)
canvas_mypass.pack()

window_welcome.mainloop()