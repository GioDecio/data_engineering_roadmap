import random
import time


def insertion_sort_ineff(array):

    for i, _ in enumerate(array[1:], start=1):

        while i >= 1:
            if array[i] < array[i - 1]:
                array[i] = array[i - 1]
                i -= 1
            else:
                break

        array[i] = array[i - 1]

    return array


def insertion_sort(array):

    for i in range(1, len(array)):

        position = i - 1
        temp_value = array[i]

        while position >= 0:
            if temp_value < array[position]:
                array[position + 1] = array[position]
                position -= 1
            else:
                break

        array[position + 1] = temp_value

    return array


array = [i + 1 for i in range(10)]  # random.sample(range(0, 100000), 10000)  #
print(array)

start_time = time.time()
print(f"insertion_sort_ineff: {insertion_sort_ineff(array)}")
time_taken_ineff = (time.time() - start_time) / 60
print("Time taken: --- %.5f minutes --- \n" % time_taken_ineff)

# start_time = time.time()
# print(f"insertion_sort: {insertion_sort(array)}")
# time_taken = (time.time() - start_time) / 60
# print("Time taken: --- %.5f minutes --- \n" % time_taken)
