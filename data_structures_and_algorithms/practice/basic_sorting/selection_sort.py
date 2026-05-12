def selection_sort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index]= my_list[min_index], my_list[i] 
    return my_list

my_list = [4,2,6,5,1,3]
print(selection_sort(my_list))

