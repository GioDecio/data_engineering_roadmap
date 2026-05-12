import time
import random


def get_average_of_even_numbers(array):

    even = []
    for n in array:
        if n % 2 == 0:
            even.append(n)

    avg = sum(even) / len(even)

    return avg


def get_average_of_even_numbers2(array):

    sum = 0
    count = 0
    for n in array:
        if n % 2 == 0:
            sum += n
            count += 1

    avg = sum / count

    return avg


# size = 1000000
# array = [i for i in range(size)]

exp = 7
array = random.sample(range(0, 10**exp), 10**exp)

start_time = time.time()
print(f"average_of_even_numbers: {get_average_of_even_numbers(array)}\n")
time_taken_1 = (time.time() - start_time) / 60
print("Time taken: --- %.5f minutes --- \n" % time_taken_1)

start_time = time.time()
print(f"average_of_even_numbers2: {get_average_of_even_numbers2(array)}\n")
time_taken_2 = (time.time() - start_time) / 60
print("Time taken: --- %.5f minutes --- \n" % time_taken_2)
