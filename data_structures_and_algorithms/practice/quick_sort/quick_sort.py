"""Quick Sort
Write a function called quick_sort_helper that performs the quick sort algorithm recursively 
on a list of integers.

The function should perform the following tasks:
Accept three parameters: my_list, which represents the list of integers being sorted; 
left, the index of the first element in the current partition; 
and right, the index of the last element in the current partition.

Check if the left index is less than the right index. 
If not, the function should return my_list without making any changes.

If the left index is less than the right index, 
call the previously implemented pivot function with my_list, left, and right as arguments, 
and store the returned value in a variable called pivot_index.

Make a recursive call to quick_sort_helper with my_list, 
left, and pivot_index-1 as arguments.

Make another recursive call to quick_sort_helper with my_list, 
pivot_index+1, and right as arguments.

Return the sorted my_list.
"""
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


## WRITE QUICK_SORT_HELPER FUNCTION HERE ##
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_idx = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_idx-1)
        quick_sort_helper(my_list, pivot_idx+1, right)

    return my_list


def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)




my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
    
 """