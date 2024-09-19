import tkinter

#Action on button click
def on_button_click():
    print("button clicked")

#Windows -----
window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx= 20, pady=20)

#Label ------
my_label = tkinter.Label(text="Hello World", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
#Change a label text
# my_label["text'] = 'new text'
# my_label.config(text= 'new text')

#Buttons --------
my_button = tkinter.Button(text="I'm a button")
my_button.grid(column = 1, row =1)
my_button.config(command= on_button_click)


#Entry -----
input = tkinter.Entry()
input.grid(column = 3, row=2)
#input.get() returns the Entry's string.


my_button2 = tkinter.Button(text= 'Second Button')
my_button2.grid(column = 2, row =0)

#Pack(top)
#Place(x, y)
#Grid(colum, row)


#main loop is the infinite loop that keeps the window displayed. Has to be the last line
window.mainloop()

