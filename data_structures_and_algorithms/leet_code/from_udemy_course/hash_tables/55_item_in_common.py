# WRITE ITEM_IN_COMMON FUNCTION HERE #
def item_in_common(l1,l2):

    l1_d = {}
    for element in l1:
        l1_d[element]=True

    for element in l2:
        if element in l1_d:
                return True
    return False




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
