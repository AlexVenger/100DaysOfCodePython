import pandas

alphabet = pandas.read_csv("../26.ListComprehension/nato_phonetic_alphabet.csv")

word = input("Type a word:\n").upper()

nato_dict = {value.letter: value.code for (number, value) in alphabet.iterrows()}

try:
    nato_word = [nato_dict[letter] for letter in word]
except KeyError:
    print("Type a name with only letters in it, please")
else:
    print(nato_word)
