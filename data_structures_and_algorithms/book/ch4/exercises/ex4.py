# find greatest number in an array
def main():

    def find_greatest(array):

        greatest = array[0]
        count = 0
        for n in array:
            if n > greatest:
                greatest = n
                count += 1

        return greatest, count

    array = [1, 2, 4, 6, 10]
    greatest, count = find_greatest(array)
    print(
        f"The greatest number in the array is: {greatest} \n"
        f"and it took {count} steps"
    )


if __name__ == "__main__":
    main()
