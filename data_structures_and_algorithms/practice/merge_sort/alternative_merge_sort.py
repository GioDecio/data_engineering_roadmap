"""
This solution avoids creating new lists with slicing during merge sort. 
The algorithm is modified to use indices.
Instead of slicing, pass the start and end indices to track the portion of the array being sorted.
Work with the original array throughout the recursion
Use these indices in the merge function as well.
Note that this in-place approach:
Still needs temporary arrays in the merge step
Modifies the original array instead of creating a new one
Uses less memory overall compared to the slicing approach
Is slightly more complex to implement and understand
The tradeoff is between memory usage and code readability. 
The slicing version is more "Pythonic" and easier to understand, while this version is more memory efficient 
but less intuitive.
"""


def merge(arr, start, mid, end):
    # Create temp arrays for left and right portions
    left_temp = arr[start:mid + 1]
    right_temp = arr[mid + 1:end + 1]
    
    i = 0  # Index for left_temp
    j = 0  # Index for right_temp
    k = start  # Index for original array
    
    # Merge back into original array
    while i < len(left_temp) and j < len(right_temp):
        if left_temp[i] <= right_temp[j]:
            arr[k] = left_temp[i]
            i += 1
        else:
            arr[k] = right_temp[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_temp):
        arr[k] = left_temp[i]
        i += 1
        k += 1
    
    while j < len(right_temp):
        arr[k] = right_temp[j]
        j += 1
        k += 1

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)
    return arr

# To use it:
my_list = [3, 1, 4, 2]
merge_sort(my_list, 0, len(my_list) - 1)
