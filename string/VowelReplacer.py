"""
Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
Notes
All characters will be in lower case.
"""


def replace_vowels(txt, ch):
    vowels: tuple = ('a', 'e', 'i', 'o', 'u')
    for v in vowels:
        txt = txt.replace(v, ch)
    return txt


def replace_vowels_join(txt, ch):
    return ''.join([char if char not in 'aeiou' else ch for char in txt])


def replace_vowels_reg(txt, ch):
    import re
    return re.sub(r'[aeiouAEIOU]', ch, txt)


print(replace_vowels("the aardvark", "#"))  # "th# ##rdv#rk"
print(replace_vowels_reg("the aardvark", "#"))  # "th# ##rdv#rk"
print(replace_vowels_join("the aardvark", "#"))  # "th# ##rdv#rk"

print(replace_vowels("minnie mouse", "?"))  # "m?nn?? m??s?"
print(replace_vowels_reg("minnie mOusE", "?"))  # "m?nn?? m??s?"
print(replace_vowels_join("minnie mouse", "?"))  # "m?nn?? m??s?"

print(replace_vowels("shakespeare", "*"))  # "sh*k*sp**r*"
print(replace_vowels_reg("shakespeare", "*"))  # "sh*k*sp**r*"
print(replace_vowels_join("shakespeare", "*"))  # "sh*k*sp**r*"
