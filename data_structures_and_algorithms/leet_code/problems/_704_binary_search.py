def search( nums, target): 
    """ 
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    lower = 0
    upper = len(nums)-1

    while lower <= upper:
        mid =int((lower + upper)/2)
        print(f"mid: {mid}") 
        mid_v = nums[mid]

        if nums[mid] == target:
            return mid 
        
        if mid_v >= target:
            upper = mid -1 
        else:
            lower = mid + 1

    return -1 
            
        

nums = [2,3,4,5,6]
target = 5
print(search(nums, target))
