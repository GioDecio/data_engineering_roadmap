"""
The function should perform the following tasks:
Accept three parameters: my_list, which represents the list of integers being sorted; pivot_index, the index of the pivot element; and end_index, the index of the last element in the list.
Initialize a variable swap_index to the value of pivot_index.
Iterate through the elements of my_list from pivot_index+1 to end_index+1 (inclusive) using a loop with the variable i.
Inside the loop, if the current element my_list[i] is less than the pivot element my_list[pivot_index], increment swap_index and call the previously implemented swap function to swap the elements at swap_index and i.
After the loop, call the swap function to swap the elements at pivot_index and swap_index.
Return the updated value of swap_index as the new pivot index.
"""

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


## WRITE PIVOT FUNCTION HERE ##
def pivot(my_list, pivot_idx, end_idx):
    swap_index = pivot_idx
    for i in range(pivot_idx+1, end_idx+1):
        if my_list[i] < my_list[pivot_idx]:
            swap_index +=1
            swap(my_list, swap_index, i)
    
    swap(my_list, pivot_idx, swap_index)

    return swap_index
    




my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6)

print('\nList after running pivot():')
print(my_list)

print('\nReturned Swap Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Returned Swap Index:
    3

 """