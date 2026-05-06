def sortArray(nums): 
    for i in range(len(nums)-1): 
        min_idx =i
        for j in range(i, len(nums)):
            
            if nums[min_idx] > nums[j]:
                min_idx = j
                
        if min_idx != i:
            nums[i], nums[min_idx]  = nums[min_idx], nums[i]

    return nums 

nums = [4,2,7,1,3]

print(f"nums is: {nums}\n")
print(f"sorted array is: {sortArray(nums)}")

