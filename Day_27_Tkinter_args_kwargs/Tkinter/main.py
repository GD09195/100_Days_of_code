import tkinter


window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Hello World", font=("Arial", 24, "bold"))



#main loop is the infinite loop that keeps the window displayed. Has to be the last line
window.mainloop()

