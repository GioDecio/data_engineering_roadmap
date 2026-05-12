def running_sum(nums):
    for idx in range(1, len(nums)):
        nums[idx] = nums[idx] + nums[idx - 1]
    return nums


my_list = [1, 2, 3, 4]

print(running_sum(my_list))
