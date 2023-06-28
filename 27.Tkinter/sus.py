import tkinter
from PIL import Image, ImageTk
import random

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

images = ["red_sus.png", "blue_sus.png", "green_sus.png"]


# Image (using PIL)
def sus():
    image = Image.open("./sus/" + random.choice(images))
    image.resize((50, 50), Image.LANCZOS)
    test_image = ImageTk.PhotoImage(image)
    label1["image"] = test_image
    label1.image = test_image
    label["text"] = entry.get()


# Button
button = tkinter.Button(text="Show Sus", command=sus)
button.pack()

# Label
label = tkinter.Label(text="", font=("Arial", 24, "bold"))
label.pack()

# Input
entry = tkinter.Entry()
entry.pack()

label1 = tkinter.Label()
label1.pack()

window.mainloop()
