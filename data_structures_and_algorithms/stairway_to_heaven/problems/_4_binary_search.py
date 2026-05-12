def binary_search(search_list, value):

    l = 0
    r = len(search_list) - 1

    while l <= r:
        mid = (r + l) // 2
        mid_value = search_list[mid]
        if mid_value == value:
            return value
        elif value > mid_value:
            l = mid + 1
        else:
            r = mid - 1

    return None
