"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


def isHappy_dict_string(n):
    """
    :type n: int
    :rtype: bool
    """
    sq_sums_dict = {}

    def get_digits(key_n):
        sq_sums = 0
        for digit in str(key_n):
            sq_sums += int(digit) ** 2

        sq_sums_dict[key_n] = sq_sums

        return sq_sums_dict[key_n]

    while True:
        if n == 1:
            return True
        if n in sq_sums_dict:
            return False
        n = get_digits(n)


def isHappy_set_string(n):
    seen = set()

    def get_digits(key_n):
        sq_sums = 0
        for digit in str(key_n):
            sq_sums += int(digit) ** 2

        seen.add(key_n)

        return sq_sums

    while True:
        if n == 1:
            return True
        if n in seen:
            return False
        n = get_digits(n)


test_cases = [2, 19, 13, 10, 1, 0]
outputs = [False, True, True, True, True, False]
for test_case, output in zip(test_cases, outputs):
    print(
        f"Dictionary: Input {test_case}: out:{isHappy_dict_string(test_case)} - exp: {output}"
    )

    print(
        f"Set: Input {test_case}: out:{isHappy_set_string(test_case)} - exp: {output}\n"
    )
