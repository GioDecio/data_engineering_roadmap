def closest_to_zeroOnSq(nums):

    abs_nums = [abs(n) for n in nums]
    candidates = [n for n in nums if abs(n) == min(abs_nums)]
    print(candidates)
    return max(candidates)


def closest_to_zeroOnWithGenerator(nums: list) -> float:
    min_abs = min(abs(n) for n in nums)
    candidates = [n for n in nums if abs(n) == min_abs]
    return max(candidates)


def closest_to_zeroOverWriteList(nums: list) -> float:
    for i in range(len(nums)):
        if nums[i] < 0 and abs(nums[i]) in nums:
            nums[i] = abs(nums[i])
    nums_abs = [abs(n) for n in nums]
    min_abs = min(nums_abs)

    return nums[nums_abs.index(min_abs)]


def closest_to_zeroDupRemoval(ts):

    # remove "duplicates"
    seen = set()
    for t in ts:
        if abs(t) not in seen:
            seen.add(abs(t))

        elif t < 0 and abs(t) in seen:
            ts.remove(t)

    # return the element of the list whose abs is smallest
    abs_ts = [abs(t) for t in ts]
    d = dict(zip(abs_ts, ts))
    min_abs_ts = min(abs_ts)
    return d[min_abs_ts]


def closest_to_zeroHashKey(ts):
    seen = {}
    for t in ts:
        if abs(t) not in seen or t > seen[abs(t)]:
            seen[abs(t)] = t
    return min(seen.values(), key=abs)


def closest_to_zeroHashSortedKey(ts):
    seen = {}
    for t in ts:
        if abs(t) not in seen or t > seen[abs(t)]:
            seen[abs(t)] = t
    return sorted(seen.values(), key=abs)[0]


def closest_to_zero(ts):
    seen = {}
    for t in ts:
        if abs(t) not in seen or t > seen[abs(t)]:
            seen[abs(t)] = t
    min_abs = sorted(seen.keys())[0]
    return seen[min_abs]


def closest_to_zeroOneMore(ts):

    _min = min(abs(t) for t in ts)
    candidates = [t for t in ts if abs(t) == _min]
    return max(candidates)
