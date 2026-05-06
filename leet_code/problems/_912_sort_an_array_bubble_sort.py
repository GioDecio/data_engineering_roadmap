def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sorted = False 
    l = len(nums)
    cnt = 0
    while not sorted:
        print(sorted)
        sorted = True
        for i in range(l-1):
            print(f"i: {i}")
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                sorted =False
        l-=1
        
        
        print(f"cnt is: {cnt}")
        cnt+=1
    return nums

nums = [65, 55, 45, 35, 25, 15, 10]
print(nums)
print(sortArray(nums))
