def print_n_in_array(arr):
    for item in arr:
        if isinstance(item, list):
            print_n_in_array(item)
        else:
            print(item)


arr = [
    1,
    2,
    [3, 4],
    [
        5,
        6,
        [7, 8, 9, [10, [11, 12, 13, 14]]],
    ],
]


print_n_in_array(arr)
