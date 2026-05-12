def linear_search_pythonic(array, search_value):

    if search_value in array:
        return True
    return False


def linear_search_apythonic_break(array, search_value):

    for n in array:
        if n == search_value:
            return True

        elif n > search_value:
            break

    return False


def linear_search_apythonic_nobreak(array, search_value):

    for n in array:

        if n > search_value:
            return False
        elif n == search_value:
            return True

    # return False


exp = int(input())
n_items = 10**exp
array = [1, 2, 44, 99]  # [i for i in range(n_items)]

print(linear_search_apythonic_nobreak(array, 3))
