from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 0
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button():
    window.after_cancel(timer)
    canvas.itemconfig(set_count,text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def reset_timer():
    global rep

    work_sec = WORK_MIN * 60
    short_sec_break = SHORT_BREAK_MIN * 60
    long_sec_break = LONG_BREAK_MIN * 60

    rep += 1
    if rep % 8 == 0:
        timer_label.config(text="Break",fg=RED)
        count_down(long_sec_break)
    elif rep % 2 == 0:
        count_down(short_sec_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(set_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        reset_timer()
        mark = ""
        sessions = math.floor(rep/2)
        for _ in range(sessions):
            mark += "✔"
        tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(104, 118, image=tomato_image)
set_count = canvas.create_text(104, 130, text="00:00", font=(FONT_NAME, 40, "bold"), fill="White")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

tick_label = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
tick_label.grid(row=3, column=1)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_button)
reset_button.grid(row=2, column=2)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
start_button.grid(row=2, column=0)

window.mainloop()
