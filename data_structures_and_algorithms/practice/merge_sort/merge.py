## WRITE MERGE FUNCTION HERE ##
def merge(list_1, list_2):
    combined = []
    i,j = 0, 0
    while i <len(list_1) and j <len(list_2): #while runs as long as there are items in ONE list.
        if list_1[i] > list_2[j]:
            combined.append(list_2[j])
            j+=1
        else:
            combined.append(list_1[i])
            i+=1
        print(j,len(list_2))
    while i<len(list_1):
        combined.append(list_1[i]) 
        i+=1
    while j<len(list_2):
        combined.append(list_2[j])
        j+=1
    return combined






print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
    
 """