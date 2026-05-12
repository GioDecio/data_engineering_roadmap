from random import choice
import random
import time


def main():

    array = [7, 4, 3, 2, 1]
    print(f"array before sorting: {array[:10]}\n")

    sorted = False
    tmp_idx = len(array) - 1
    count = 0
    n_loops = 0
    while not sorted:
        sorted = True
        for idx in range(tmp_idx):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                count += 1
                sorted = False
        tmp_idx -= 1
        n_loops += 1

    print(f"Counts: {count}\n")
    print(f"Loops: {n_loops}\n")
    print(f"array after sorting: {array[:10]}.\n")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Time taken: --- %.5f minutes ---" % ((time.time() - start_time) / 60))
