"""
Reverse the Odd Length Words
Given a string, reverse all the words which have odd length. The even length words are not changed.

Examples
reverse_odd("Bananas") ➞ "sananaB"

reverse_odd("One two three four") ➞ "enO owt eerht four"

reverse_odd("Make sure uoy only esrever sdrow of ddo length")
➞ "Make sure you only reverse words of odd length"
Notes
There is exactly one space between each word and no punctuation is used.
"""


## one line
## 	return ' '.join(i[::-1] if len(i)%2 else i for i in txt.split())

def reverse_odd(txt):
    words = txt.split()
    result = []
    for word in words:
        result.append(word[::-1]) if len(word) % 2 != 0 else result.append(word)
    return ' '.join(result)


print(reverse_odd("Bananas"))  # "sananaB"
print(reverse_odd("One two three four"))  # "enO owt eerht four"
print(reverse_odd("Make sure uoy only esrever sdrow of ddo length"))  # "Make sure you only reverse words of odd length"
