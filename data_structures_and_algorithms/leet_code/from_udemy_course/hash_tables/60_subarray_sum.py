def subarray_sum_inefficient(nums, target):

    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i:]):
            if sum(nums[i:j+1])==target:
                print(sum(nums[i:j+1]))
                return [i, j]
    return []

def subarray_sum(nums, target):
    prefix_sum = 0
    #sum_dict = {0:-1}
    sum_dict = {}
    for idx, num in enumerate(nums):
        prefix_sum +=num
        if prefix_sum - target in sum_dict:
            print(sum_dict)
            return [sum_dict[prefix_sum-target]+1, idx]
        sum_dict[prefix_sum]=idx 
    return []
        

    


# nums = [1, 2, 3, 4, 5]
# target = 9
# print ( subarray_sum(nums, target) )

# nums = [-1, 2, 3, -4, 5]
# target = 0
# print ( subarray_sum(nums, target) )

# nums = [2, 3, 4, 5, 6]
# target = 3
# print ( subarray_sum(nums, target) )

nums = [1,2,3]
target = 3
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""