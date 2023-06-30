from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGES = {
    "Spanish": "./data/spanish_words.csv",
    "French": "./data/french_words.csv"
}  # Update if any other languages are available

words = []
guessed_words = []
words_to_guess = []
translation = None


def select_language():
    global words
    try:
        words = pandas.read_csv(f"./data/words_to_learn_{language_var.get().lower()}.csv").to_dict(orient="records")
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        try:
            words = pandas.read_csv(LANGUAGES[language_var.get()]).to_dict(orient="records")
        except KeyError:
            messagebox.showerror(title="No Words!", message="You don't have any files for the selected language!")
            language_window.destroy()
            window.destroy()
        else:
            language_window.destroy()
            window.deiconify()
            pick_a_word()
    else:
        language_window.destroy()
        window.deiconify()
        pick_a_word()


def show_translation(word_to_guess):
    canvas.itemconfig(language, text="English", fill="White")
    canvas.itemconfig(word, text=word_to_guess["English"], fill="White")
    canvas.itemconfig(background, image=card_back)


def pick_a_word():
    global translation
    selected_language = language_var.get()
    if len(words) == 0:
        return
    n = random.randint(0, len(words) - 1)
    word_to_guess = words[n]
    canvas.itemconfig(language, text=selected_language, fill="Black")
    canvas.itemconfig(word, text=words[n][selected_language], fill="Black")
    canvas.itemconfig(background, image=card_front)
    translation = window.after(3000, show_translation, word_to_guess)
    return word_to_guess


def pick_a_word_correct():
    global translation
    window.after_cancel(translation)
    guessed_word = pick_a_word()
    words.remove(guessed_word)
    guessed_words.append(guessed_word)
    print(guessed_word)


def pick_a_word_wrong():
    global translation
    window.after_cancel(translation)
    guessed_word = pick_a_word()
    words_to_guess.append(guessed_word)
    print(words_to_guess)


window = Tk()
window.title("Vocabulary++")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
background = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

yes_image = PhotoImage(file="./images/right.png")
no_image = PhotoImage(file="./images/wrong.png")

yes_button = Button(image=yes_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=pick_a_word_correct)
yes_button.grid(row=1, column=1)

no_button = Button(image=no_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=pick_a_word_wrong)
no_button.grid(row=1, column=0)

# Language selection window
language_window = Toplevel(window)
language_window.title("Select Language")
language_window.attributes("-topmost", True)
language_window.config(padx=100)

# Variable to keep the selected language
language_var = StringVar()

# Radio buttons for different languages. Each language requires another one
spanish_radio = Radiobutton(language_window, text="Spanish", variable=language_var, value="Spanish")
spanish_radio.pack()

french_radio = Radiobutton(language_window, text="French", variable=language_var, value="French")
french_radio.pack()

russian_radio = Radiobutton(language_window, text="Russian", variable=language_var, value="Russian")
russian_radio.pack()

# Button for language confirmation
language_confirm_button = Button(language_window, text="Select", command=select_language)
language_confirm_button.pack()

window.mainloop()

# Saving unguessed words to words_to_learn file
words_to_guess_df = pandas.DataFrame(data=words_to_guess)
if len(words_to_guess_df) > 0:
    words_to_guess_df.to_csv(f"./data/words_to_learn_{language_var.get().lower()}.csv", index=False)

# Adding guessed words to guessed_words file
try:
    guessed_words_dict = pandas.read_csv(f"./data/guessed_words_{language_var.get().lower()}.csv")\
        .to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    guessed_words_dict = pandas.DataFrame(data=guessed_words).to_dict(orient="records")
else:
    new_guessed_words = pandas.DataFrame(data=guessed_words).to_dict(orient="records")
    guessed_words_dict += new_guessed_words
finally:
    pandas.DataFrame(guessed_words_dict).to_csv(f"./data/guessed_words_{language_var.get().lower()}.csv", index=False)
