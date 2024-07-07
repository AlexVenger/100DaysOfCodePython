from morse_code import MORSE_CODE, MORSE_CODE_REVERSE


def converter(text_line: str):
    symbols = set(text_line)
    if symbols.issubset({"-", ".", " ", "\t"}):
        return morse_to_text_converter(text_line)
    else:
        return text_to_morse_converter(text_line)


def text_to_morse_converter(text: str):
    morse = ""
    for symbol in text.lower():
        if symbol in MORSE_CODE.keys():
            morse += MORSE_CODE[symbol]
            morse += " "
    return morse


def morse_to_text_converter(morse: str):
    text = ""
    codes = morse.split(" ")
    for code in codes:
        if code in MORSE_CODE_REVERSE.keys():
            text += MORSE_CODE_REVERSE[code]
    return text


line = str(input("Write your text to convert it to Morse code (latin letters and digits only)\n"))
print(converter(line))
