import tkinter


def miles_to_kilometers():
    result["text"] = round(float(entry.get()) * 1.609, 2)


window = tkinter.Tk()
window.title("Mile to Kilometers")
window.minsize(width=200, height=100)
window.config(padx=20, pady=10)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

from_unit = tkinter.Label(text="Miles")
from_unit.grid(column=2, row=0)

to_unit = tkinter.Label(text="Kilometers")
to_unit.grid(column=2, row=1)

equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)

result = tkinter.Label(text="")
result.grid(column=1, row=1)

calculation_button = tkinter.Button(text="Calculate", command=miles_to_kilometers)
calculation_button.grid(column=1, row=2)

window.mainloop()
