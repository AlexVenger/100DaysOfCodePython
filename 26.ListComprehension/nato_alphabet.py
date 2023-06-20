import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

word = input("Type a word:\n").upper()

nato_dict = {value.letter: value.code for (number, value) in alphabet.iterrows()}

nato_word = [nato_dict[letter] for letter in word]
print(nato_word)
