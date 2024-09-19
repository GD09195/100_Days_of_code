import tkinter

def action_calculate():
    mi = float(user_mi_entry.get())
    km = (mi*8)/5
    km_number_label.config(text=km)

window = tkinter.Tk()
window.title("mi to km converter")
window.minsize(width=10, height=10)
window.config(padx=20, pady=20)

# 'is equal to' Label
equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(column= 0, row=1)

#'miles' label
miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

#km label
km_number_label = tkinter.Label(text='0')
km_number_label.grid(column=1, row= 1)

#'km' label
km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

#Miles Entry
user_mi_entry = tkinter.Entry(width=8)
user_mi_entry.grid(column=1, row=0)

#'Calculate' button
calculate_button = tkinter.Button(text='Calculate',command=action_calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()