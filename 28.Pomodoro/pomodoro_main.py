from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

break_count = 0
timer = None
break_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    if timer is not None:
        timer_title.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
        global break_count
        break_count = 0
        window.after_cancel(timer)
        window.after_cancel(break_timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if canvas.itemcget(timer_text, "text") == "00:00":
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def show_time(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")


def countdown(count):
    show_time(count)
    timer_title.config(text="Work", fg=GREEN)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        global break_count
        break_count += 1
        break_time(0)


def break_time(count):
    show_time(count)
    check_mark["text"] = "✔" * (break_count // 2)
    break_length = SHORT_BREAK_MIN * 60
    timer_title.config(text="Break", fg=PINK)
    if break_count % 4 == 0:
        break_length = LONG_BREAK_MIN * 60
        timer_title["fg"] = RED
    if count < break_length:
        global break_timer
        break_timer = window.after(1000, break_time, count + 1)
    else:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        countdown(WORK_MIN * 60)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "normal"))
timer_title.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "normal"))
check_mark.grid(row=3, column=1)

window.mainloop()
