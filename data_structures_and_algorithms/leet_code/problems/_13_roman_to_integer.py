"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    n = 0
    i = len(s) - 1
    while i > -1:
        # print(f"i:{i}")
        if i != 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
            # print("?")
            temp = roman_dict[s[i]] - roman_dict[s[i - 1]]
            i -= 2
        else:
            # print("ciao")
            temp = roman_dict[s[i]]
            i -= 1

        n += temp
        # print(f"temp: {temp}")
        # print(f"n:{n}\n")

    return n


inputs = ["I", "II", "IV", "LVIII", "MCMXCIV"]
outputs = [1, 2, 4, 58, 1994]

for input, output in zip(inputs, outputs):
    if input in inputs:
        # print(input, output)
        print(f"Out:{romanToInt(input)} - Exp: {output}")
        # print(romanToInt(input))
