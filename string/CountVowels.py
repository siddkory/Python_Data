"""
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
Notes
a, e, i, o, u are considered vowels (not y).
All test cases are one word and only contain letters.
"""


def count_one_line(txt):
    return sum(c in "aeiou" for c in txt)


def count_vowels(txt):
    vowels = [vowel for vowel in txt if vowel in 'aeiou']
    print(vowels)
    return len(vowels)


def count_vowels_regex(txt):
    import re
    return len(re.findall(r'[aeiou]', str))


print(count_vowels("Celebration"))
print(count_vowels("Palm"))
print(count_vowels("Prediction"))
