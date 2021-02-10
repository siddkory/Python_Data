"""
Game of Thrones: Character Titles
Write a function that takes a string and returns a string with the correct case for character titles in the Game of Thrones series.

The words and, the, of and in should be lowercase.
All other words should have the first character as uppercase and the rest lowercase.
Examples
correct_title("jOn SnoW, kINg IN thE noRth.")
➞ "Jon Snow, King in the North."

correct_title("sansa stark, lady of winterfell.")
➞ "Sansa Stark, Lady of Winterfell."

correct_title("TYRION LANNISTER, HAND OF THE QUEEN.")
➞ "Tyrion Lannister, Hand of the Queen."
Notes
Punctuation and spaces must remain in their original positions.
Hyphenated words are considered separate words.
Be careful with words that contain and, the, of or in.
See the Resources tab for more info on the various Python string methods.

    # pattern = re.compile(r"\b((?!in)(?!the).)*\s\b", re.I)

"""

from collections import OrderedDict
import re


def correct_title(txt):
    pattern = re.compile(r"([a-zA-Z]+)('[a-zA-Z])?")
    result = pattern.sub(lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower() if mo.group(0).lower() not in (
        'and', 'the', 'of', 'in') else mo.group(0).lower(), txt)
    return result


def correct_title_strtitle(txt):
    title_txt = txt.title()
    replace = OrderedDict([('And ', 'and '), ('The ', 'the '), ('Of ', 'of '), ('In ', 'in ')])
    return replace_all(replace, title_txt)


def replace_all(replace_dict: OrderedDict, txt: str):
    for i, j in replace_dict.items():
        txt = txt.replace(i, j)
    return txt


print(correct_title("jOn SnoW, kINg IN thE noRth. Jon doesn't know anything "))  # "Jon Snow, King in the North."
print(correct_title("Cersei Lannister, Queen of the andals and the First Men, Protector of the Seven Kingdoms."))

"""
Cersei Lannister, Queen of the andals and the First Men, Protector of the Seven Kingdoms.' 
Cersei Lannister, Queen of the Andals and the First Men, Protector of the Seven Kingdoms.'

print(correct_title("sansa stark, lady of winterfell."))  "Sansa Stark, Lady of Winterfell.
# print(correct_title("TYRION LANNISTER, HAND OF THE QUEEN."))  # Tyrion Lannister, Hand of the Queen."
"""
