"""
Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number.
To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value,
value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

Examples
binary(1) ➞ "1"
# 1*1 = 1

binary(5) ➞ "101"
# 1*1 + 1*4 = 5

binary(10) ➞ "1010"
# 1*2 + 1*8 = 10
Notes
Numbers will always be below 1024 (not including 1024).
The strings will always go to the length at which the most left bit's value gets bigger than the number in decimal.
If a binary conversion for 0 is attempted, return "0".


https://realpython.com/convert-python-string-to-int/

"""


# def binary(decimal):
#     num = str(int(decimal, base=8))
#     print(num)
#     return int(num, 2)
#     #return f"{decimal:b}"
#     #return int(decimal, base=8)

def convertor(num_str, ret_base):
    base = "decimal"
    base_num = 10
    if num_str.startswith("0b"):
        base = "binary"
        base_num = 2
    elif num_str.startswith("0o"):
        base = "oct"
        base_num = 8
    elif num_str.startswith("0x"):
        base = "hex"
        base_num = 16

    num = int(num_str) if base == "decimal" else int(num_str, base=base_num)
    if num == 0:
        return "0"
    elif ret_base == "binary":
        return str(bin(num))
    elif ret_base == "hex":
        return str(hex(num))
    elif ret_base == "oct":
        return str(oct(num))
    return str(num)


print("----------------------")
print("Decimal to other base")
print(convertor("1234", "decimal"))
print(convertor("1234", "oct"))
print(convertor("1234", "hex"))
print(convertor("1234", "binary"))

print("----------------------")
print("Other base to decimal")
print(convertor("0b10110100101011101001110", "decimal"))
print(convertor("0xabcdef", "decimal"))
print(convertor("0o316271271", "decimal"))
print(convertor("0o7777", "decimal"))
