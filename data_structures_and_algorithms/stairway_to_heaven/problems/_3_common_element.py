# Problema: date due liste, dimmi se hanno almeno un elemento in comune.


def common_element(l_1, l_2):

    for c_1 in l_1:
        if c_1 in l_2:
            return True

    return False


def common_elementSetBug(l_1, l_2):

    for c_1 in l_1:
        if c_1 in set(l_2):
            return True

    return False


def common_elementSet(l_1, l_2):

    l2_set = set(l_2)
    for c_1 in l_1:
        if c_1 in l2_set:
            return True

    return False
