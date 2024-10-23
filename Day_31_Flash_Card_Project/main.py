import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

words_dataframe: pd.DataFrame = pd.DataFrame()
random_word: dict = {}
words_list: list[dict] = []


def flip_card()->None:
    global random_word

    canvas.itemconfig(canvas_image, image=image_card_back)
    canvas.itemconfig(language_label, fill= 'white', text='English')
    canvas.itemconfig(word_label,fill= 'white', text=random_word['English'])


def get_randon_word()-> None:
    global random_word, flipped_timer

    window.after_cancel(flipped_timer)

    canvas.itemconfig(canvas_image, image=image_card_front)
    random_word = random.choice(words_list)
    canvas.itemconfig(language_label,fill='black', text= 'French')
    canvas.itemconfig(word_label,fill='black', text=random_word['French'])

    flipped_timer= window.after(3000, func=flip_card)


def right_answer() -> None:

    words_list.remove(random_word)
    pd.DataFrame(words_list).to_csv('./data/words_to_learn.csv', index=False)
    get_randon_word()

#-----------------Open Save file ----------------------------------
try:
    words_dataframe: pd.DataFrame = pd.read_csv('./data/words_to_learn.csv')

except FileNotFoundError:
    words_dataframe: pd.DataFrame = pd.read_csv('./data/french_words.csv')

finally:
    words_list: list = words_dataframe.to_dict(orient='records')


#-----------------Tk Window-------------------------------
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flipped_timer = window.after(3000, func= flip_card)

#-----------------Tk Canvas-------------------------------
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_card_front = tkinter.PhotoImage(file='./images/card_front.png')
image_card_back = tkinter.PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image= image_card_front)
canvas.grid(column=0, row=0, columnspan=2)

#-----------------Tk Labels-------------------------------
language_label = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word_label = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

#-----------------Tk Buttons-------------------------------
#Right button
image_right = tkinter.PhotoImage(file='./images/right.png')
button_right = tkinter.Button(image=image_right,command=right_answer, highlightthickness=0)
button_right.grid(column=1, row=1)

#Wrong button
image_wrong = tkinter.PhotoImage(file='./images/wrong.png')
button_wrong = tkinter.Button(image=image_wrong, command=get_randon_word ,highlightthickness=0)
button_wrong.grid(column=0, row=1)


get_randon_word()

window.mainloop()