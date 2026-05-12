# You are given an integer array nums. The unique elements of an array are the elements that appear
# exactly once in the array.
# Return the sum of all the unique elements of nums.


def sumOfUniqueTwoLoops(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = 0
    d = {}

    for n in nums:
        cnt = 1
        if n in d:
            cnt += 1
        d[n] = cnt

    for n in d:
        if d[n] == 1:
            res += n

    return res



def sumOfUnique(nums):
    d = {}
    res = 0

    for n in nums:
        if n not in d:
            d[n]=True
            res +=n
        else:
            if d[n]:
                res -=n
                d[n]=False
    return res


nums = [1, 1, 1, 1]

print(sumOfUnique(nums))
