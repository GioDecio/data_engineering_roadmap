import random


def selection_sort(array):

    for i, _ in enumerate(array):
        lowest_idx = i
        for j in range(i + 1, len(array)):
            if array[lowest_idx] > array[j]:
                lowest_idx = j

        if lowest_idx != i:
            temp = array[i]
            array[i], array[lowest_idx] = (
                array[lowest_idx],
                array[i],
            )

    return array


array = random.sample(range(0, 30), 10)
print(f"Not ordered array: {array}")
print(f"Ordered array: {selection_sort(array)}")
