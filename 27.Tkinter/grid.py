from tkinter import *


def change_label():
    label["text"] = entry.get()


def change_button_text():
    if button1["text"] == "New Button":
        button1["text"] = "Old Button"
    else:
        button1["text"] = "New Button"


window = Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)

button = Button(text="Click", command=change_label)
button.grid(column=1, row=1)

label = Label(text="Hello!", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

entry = Entry()
entry.grid(column=3, row=3)

button1 = Button(text="New Button", command=change_button_text)
button1.grid(column=2, row=0)

window.mainloop()
