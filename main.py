import tkinter as tk
import time
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
# VARIABLES
checkmark = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Resets the timer at zero."""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=RED)
    checkmark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Begins the timer."""
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Break!", fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text="Work!", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Displays the timer countdown on the screen."""
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += checkmark
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro!")
window.config(padx=100, pady=50, bg=GREEN)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=RED)
timer_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_pic = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = tk.Label(bg=GREEN, fg=RED)
checkmark_label.grid(column=1, row=3)

window.mainloop()
