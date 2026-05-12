def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        #print(f"Loop number:{i}")
        for j in range(i):
            #print(j)
            if my_list[j]>my_list[j+1]:
                temp = my_list[j]
                my_list[j]= my_list[j+1]
                my_list[j+1]= temp
                
    return my_list


def bubble_sort_mine(my_list):
    cycle = len(my_list) - 1
    sorted = False 
    while not sorted:
        sorted = True 
        for j in range(cycle):
            if my_list[j] > my_list[j+1]: 
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                sorted=False
        cycle -=1
        if sorted:
            break
    return my_list

def bubble_sort_book(my_list):
    cycle = len(my_list) - 1
    sorted = False 
    while not sorted:
        sorted = True
        for j in range(cycle):
            if my_list[j] > my_list[j+1]: 
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            sorted = False
        cycle -=1
    return my_list




my_list = [4, 2, 6, 5, 1, 3]            
print(bubble_sort_book(my_list))
bubble_sort_book(my_list)