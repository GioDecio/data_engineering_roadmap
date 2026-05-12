# Given an integer num, repeatedly add all its digits
# until the result has only one digit, and return it.


def addDigits(num):
    """
    :type num: int
    :rtype: int
    """

    if num // 10 == 0:
        return num

    sum_d = 0
    while num > 0:
        dig = num % 10  # Get the last digit
        sum_d += dig  #  Add it to the sum
        num //= 10  # Remove the last digit

    return addDigits(sum_d)
