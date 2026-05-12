def item_in_common(l1,l2):

    l1_d = {}
    for element in l1:
        l1_d[element]=True

    for element in l2:
        if element in l1_d:
                return True
    return False



l1 = [1,3,5]
l2=[2,4,6,6,5]

print(item_in_common(l1, l2))