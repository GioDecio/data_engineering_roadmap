def binary_search(array, search_value):

    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:

        mid = int((lower_bound + upper_bound) / 2)

        mid_value = array[mid]

        if search_value == mid_value:
            return True
        elif search_value < mid_value:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return False


n = 5
array = [1, 23, 100, 900, 10**8]

print(array)
print(binary_search(array, 900))
