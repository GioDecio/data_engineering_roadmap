"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    print('\n')
    s = s.replace(' ', '') 
    print(f"s: {s}")
    left = 0
    right = len(s)-1 
    
    while right>=left:

        print(left, right)
        print(s[left], s[right])
        if s[left].lower() !=s[right].lower():
            return False

        left+=1 
        right-=1

    return True

inputs = ['race a car','A man, a plan, a canal: Panama','ama','abba', 'gatto']
for input in inputs:
    print(is_palindrome(input))
