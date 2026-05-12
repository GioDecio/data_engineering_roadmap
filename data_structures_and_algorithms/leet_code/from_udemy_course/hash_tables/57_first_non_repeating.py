def first_non_repeating_char(s):

    char_dict = {}

    for char in s:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]= 1
    
    print(char_dict)

    for char in s:
        if char_dict[char]==1:
            return char 
        
    return None

    
print(first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('abc') )


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""


d = {'a': 0, 'b': 1}

# Without default value
print(d.get('a'))      # returns 0
print(d.get('c'))      # returns None
if 0:         # This condition is False even though 'a' exists!
    print("exists")

# With default value
print(d.get('a', 0))   # returns 0
print(d.get('c', 0))   # returns 0
