def sortArray(nums):
    for i in range(len(nums)-1):
        temp = nums[i+1]
        j = i
        while j>=0:
            # Keep comparing elements to the left of the gap with temp
            # Until you reach the far left end or
            # nums[j] is <= temp, which means one element to the left of the gap is smaller than temp.
            # The partition to the left is already sorted in that case.
            if nums[j] > temp:
                nums[j+1] = nums[j]
            else:
                break
            # Insert temp into the gap now that the comparison is ended.
            nums[j] = temp   
            j-=1

    return nums

nums = [100, 0, -90, 6,12,34,23,79,4,2,7,1,3]

print(sortArray(nums))
