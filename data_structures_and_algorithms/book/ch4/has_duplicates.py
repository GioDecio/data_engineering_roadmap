import time
import random


def main():
    def has_duplicates_quadratic(array):

        for i, _ in enumerate(array):
            for j, _ in enumerate(array):
                if i != j and array[j] == array[i]:
                    return True

        return False

    def has_duplicates_linear(array):

        ex_numbers = {}
        for i, n in enumerate(array):
            if ex_numbers.get(array[i]) is not None:
                return True
            else:
                ex_numbers[array[i]] = 1
        return False

    def has_duplicates_average1(array):

        ex_numbers = []
        for i, n in enumerate(array):
            if n in ex_numbers:
                return True
            ex_numbers.append(n)
        return False

    def has_duplicates_set(array):

        ex_numbers = set()
        for i, n in enumerate(array):
            if n in ex_numbers:
                return True
            ex_numbers.add(n)
        return False

    # Generate n random numbers between min and max
    exp = 4
    array = random.sample(range(0, 10**exp), 10**exp)  #
    # array = [i + 1 for i in range(10000)] + [1]  #

    start_time = time.time()
    print(f"has duplicates - linear: {has_duplicates_linear(array)}")
    time_taken_linear = (time.time() - start_time) / 60
    print("Time taken: --- %.5f minutes --- \n" % time_taken_linear)

    start_time = time.time()
    print(f"has duplicates - set: {has_duplicates_set(array)}")
    time_taken_set = (time.time() - start_time) / 60
    print("Time taken: --- %.5f minutes --- \n" % time_taken_set)

    start_time = time.time()
    print(f"Has duplicates - quadratic: {has_duplicates_quadratic(array)}")
    time_taken_q = (time.time() - start_time) / 60
    print("Time taken: --- %.5f minutes --- \n" % time_taken_q)

    # print(f"set solution is {round(time_taken_q/time_taken_set,4)}x times faster")

    start_time = time.time()
    print(f"has duplicates - avg1: {has_duplicates_average1(array)}")
    time_taken_avg1 = (time.time() - start_time) / 60
    print("Time taken: --- %.5f minutes --- \n" % time_taken_avg1)

    # print(f"avg1 solution is {round(time_taken_q/time_taken_avg1,4)}x times faster")


if __name__ == "__main__":
    main()
