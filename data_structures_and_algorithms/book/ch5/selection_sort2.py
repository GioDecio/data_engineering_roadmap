def sortArray(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j]<nums[min_idx]:
                min_idx = j
        
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


nums = [4,5,2,1]
print(sortArray(nums))
            
                
