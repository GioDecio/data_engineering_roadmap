"""
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, 
you have to subtract 1 from it.
"""


def number_of_steps_standard(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        steps += 1
    return steps


def number_of_steps_bitwise(num):
    steps = 0
    while num > 0:
        if (num & 1) == 0:
            num >>= 1
        else:
            num -= 1
        steps += 1
    return steps


num = 17

print(number_of_steps_standard(num))
print(number_of_steps_bitwise(num))
