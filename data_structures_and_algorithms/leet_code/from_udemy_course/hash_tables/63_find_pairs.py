def find_pairs(arr1, arr2, target):
    pairs = []
    set2 = set(arr2)
    for n in arr1:
        if target - n in set2:
            pairs.append((n, target - n))
        
    return pairs




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""