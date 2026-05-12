def intersection(array1, array2):

    darray1 = {item: True for item in array1}

    intersection_array = [item for item in array2 if item in darray1.keys()]

    return intersection_array


array1 = "a b c d".split(" ")
array2 = "b d e".split(" ")

print(intersection(array1, array2))
