"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    d = {}

    for char in magazine:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for char in ransomNote:
        if char in d and d[char]>0:
            d[char]-=1
        else:
            return False
            
           
    return True


test_cases = {('aa','aab'):True} 

for test_case in test_cases:
    print(canConstruct(test_case[0], test_case[1]))
    try:
        assert canConstruct(test_case[0], test_case[1]) == test_cases[test_case]
    except AssertionError as e:
        print(e)
