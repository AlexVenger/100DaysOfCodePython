from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ----------------------------- PASSWORD SEARCH --------------------------------- #
def password_search():
    website = website_input.get()
    try:
        file = open("passwords.json", "r")
    except FileNotFoundError:
        messagebox.showinfo(title="No Saved Passwords", message="You haven't saved any passwords yet!")
    else:
        data = json.load(file)
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showinfo(title="Password Not Found", message="You haven't saved any passwords for this website")
        else:
            messagebox.showinfo(title=f"{website.title()}", message=f"Email: {email}\nPassword: {password}")
    finally:
        file.close()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password = password_numbers + password_symbols + password_letters
    random.shuffle(password)
    result = "".join(password)

    password_input.delete(0, END)
    password_input.insert(0, result)

    pyperclip.copy(result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Empty Field Warning", message="All fields should be filled in!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save these credentials?\n"
                                                          f"Email: {email}\nPassword: {password}")
    if not is_ok:
        return

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("passwords.json", "w") as new_file:
            json.dump(new_data, new_file, indent=4)
    else:
        with open("passwords.json", "w") as file:
            data.update(new_data)
            json.dump(data, file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)
    messagebox.showinfo(title="Done!", message="Your password has been saved!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="../29.PasswordManager/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1, columnspan=1, sticky="ew")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0, "bfg@doom.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, columnspan=2, sticky="ew")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

search_button = Button(text="Search", command=password_search)
search_button.grid(row=1, column=2, columnspan=1, sticky="ew")

window.mainloop()
