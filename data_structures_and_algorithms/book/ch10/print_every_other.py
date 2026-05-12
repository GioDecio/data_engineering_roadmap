def print_every_other(low, high):

    n = low
    while n < high + 1:
        print(n)
        n += 2


def print_every_other_rec(low, high):
    print(low)
    if low + 2 > high:
        return
    print_every_other_rec(low + 2, high)


low = 1
high = 10

print_every_other_rec(low, high)
