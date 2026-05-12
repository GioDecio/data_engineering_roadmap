"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    max_consecutive = 0
    current_consecutive = 0

    for num in nums:
        if num == 1:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0

    return max_consecutive


inputs = [[0, 0, 0, 1], [1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1]]
expected = [1, 3, 2, 2]

results = zip(inputs, expected)

for i, result in enumerate(results):
    if i >= 0:
        print(i, result)
        print(f"Out: {findMaxConsecutiveOnes(result[0])} - Exp: {result[1]}")
