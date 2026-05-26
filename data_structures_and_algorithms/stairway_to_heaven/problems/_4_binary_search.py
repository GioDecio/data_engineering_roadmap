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


def binary_search_2(search_list, value):

    _left = 0
    _right = len(search_list) - 1

    while _left <= _right:
        mid_idx = (_left + _right) // 2
        mid_value = search_list[mid_idx]

        if mid_value == value:
            return value

        elif mid_value < value:
            _left = mid_idx + 1
        else:
            _right = mid_idx - 1

    return None


class ListNotSortedError(Exception):
    pass


def binary_search_with_order_check(search_list, value):

    if search_list != sorted(search_list):
        raise ListNotSortedError("search list is NOT sorted")

    else:
        return binary_search_2(search_list, value)
