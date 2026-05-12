import random


def bubble_sort(array):

    for j, _ in enumerate(array):
        for i, _ in enumerate(array[:-j]):
            if i + 1 < len(array):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]

    return array


array = random.sample(range(0, 30), 10)
print(f"Not ordered array: {array}")
print(f"Ordered array: {bubble_sort(array)}")
