# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n in enumerate(nums):
        print(i)
        for j in range(i + 1, len(nums)):
            print(f"  j: {j}")
            n_sum = n + nums[j]
            if n_sum == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))


def twoSumHash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    d = {}
    for i, n in enumerate(nums):
        c = target - n
        if c in d:
            return [d[c], i]
        else:
            d[n] = i
