# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import re


def isPalindrome2(s):
    """
    :type s: str
    :rtype: bool
    """

    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]", "", s)

    for idx in range(len(s) // 2):
        if s[idx] != s[-idx - 1]:
            return False

    return True


s = "0P"  # " 123 Fante cAv@llo R3! "
print(isPalindrome2(s))
