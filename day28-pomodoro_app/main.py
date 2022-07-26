from tkinter import *
import time
import math

RED = "#e7305b"
COLD = "#C8B6E2"
BLUE = "#495C83"
GREEN = "#90C8AC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


def reset_timer():
    # TIMER RESET
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=COLD)
    check_marks.config(text="")


def start_timer():
    # TIMER MECHANISM
    # TODO: add pause button
    global reps

    reps += 1
    if reps % 2 == 0:
        label.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


def count_down(count):
    # COUNTDOWN MECHANISM
    global timer

    time_count = time.strftime('%M:%S', time.gmtime(count))
    canvas.itemconfig(timer_text, text=time_count)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


window = Tk()
window.title("Pomodoro App!")
window.config(padx=40, pady=30, bg=BLUE)

label = Label(text="Timer", bg=BLUE, fg=COLD, font=(FONT_NAME, 50))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=225, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer, highlightbackground=BLUE, fg=BLUE)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, highlightbackground=BLUE, fg=BLUE)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=BLUE)
check_marks.grid(row=3, column=1)

window.mainloop()
