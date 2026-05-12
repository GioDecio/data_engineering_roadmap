def sum(low, high):
    if low == high:
        return low
    return high + sum(low, high - 1)


low = 1
high = 4
print(sum(low, high))
