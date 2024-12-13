import tkinter

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self):

        # Window config
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Canvas config
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Hello World',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Label
        self.label_score = tkinter.Label(text=f'Score : ')
        self.label_score.config(background=THEME_COLOR, fg='white')
        self.label_score.grid(column=1, row=0)

        #PhotoImage
        photo_image_true = tkinter.PhotoImage(file='./images/true.png')
        photo_image_false = tkinter.PhotoImage(file='./images/false.png')

        #Buttons
        self.button_true = tkinter.Button(image= photo_image_true, highlightthickness=0)
        self.button_true.grid(column=0, row=2)

        self.button_false = tkinter.Button(image= photo_image_false, highlightthickness=0)
        self.button_false.grid(column=1, row=2)


        self.window.mainloop()


