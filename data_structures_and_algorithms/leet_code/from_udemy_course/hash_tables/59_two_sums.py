def two_sum_no_hash(n_list, S):

    for i, n in enumerate(n_list):
        if S - n in n_list[i+1:]:
            return [i, i+1+n_list[i+1:].index(S-n)]     
        
    return []

def two_sum(n_list, S):
    hash_table = {}
    for i, n in enumerate(n_list):
        if S-n in hash_table:
            return [i, hash_table[S-n]]
        else: 
            hash_table[n]=i
    return []    
    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


