import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer,text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text='Break', fg=RED)
        countdown_timer(long_break_sec)


    elif reps %2 == 0:
        label_timer.config(text='Break', fg=PINK)
        countdown_timer(short_break_sec)

    else:
        label_timer.config(text='Work', fg=GREEN)
        countdown_timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown_timer(count)->None:

    #Format: 00:00
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'


    canvas.itemconfig(text_timer, text=f'{count_min}:{count_sec}')

    if count > 0:
       global timer
       timer = window.after(1000, countdown_timer, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += '✔'
        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

#Window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=60, pady=40, bg=YELLOW)

#Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_png)
text_timer = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)


#Label 'Timer'
label_timer = tkinter.Label(text="Timer", font=(FONT_NAME, 38, 'bold'))
label_timer.config(fg=GREEN, bg=YELLOW)
label_timer.grid(column= 1, row=0)

#label '✔'
label_check = tkinter.Label(font=(FONT_NAME, 28, ))
label_check.config(fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

#button 'Start'
button_start = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)


#button 'Reset'
button_start = tkinter.Button(text='Reset',highlightthickness=0, command=reset_timer)
button_start.grid(column=2, row=2)

window.mainloop()