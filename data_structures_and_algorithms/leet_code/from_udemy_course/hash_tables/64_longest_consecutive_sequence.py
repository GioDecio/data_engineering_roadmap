def longest_consecutive_sequence_ineff(array):
    set_arr = set(array)
    lengths = []
    for num in set_arr:
        if num -1 not in set_arr:
            sequence = [num]
            while num + 1 in set_arr:
                num +=1
                sequence.append(num)
            lengths.append(len(sequence))
        
    try: 
        return max(lengths)
    except ValueError:
        return 0

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence 



print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""