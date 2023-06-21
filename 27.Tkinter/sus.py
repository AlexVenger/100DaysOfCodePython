import tkinter
import turtle
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="SUS", font=("Arial", 24, "bold"))
label.pack()

# Image (using PIL)
image = Image.open("sus.png")
image.resize((50, 50), Image.ANTIALIAS)
test_image = ImageTk.PhotoImage(image)
label1 = tkinter.Label(image=test_image)
label1.image = test_image
label1.pack()

window.mainloop()
