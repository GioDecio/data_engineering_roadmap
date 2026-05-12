def find_pair(array):

    darray = {}

    for item in array:
        if darray.get(item):
            return item
        else:
            darray[item] = True

    return False


array = "a b c e f a".split(" ")
# print(array)
print(find_pair(array))
