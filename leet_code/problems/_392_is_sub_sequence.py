"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) > len(t):
        return False

    cnt = 0
    i = 0
    for cs in s:
        if cs in t[i:]:
            cnt += 1
            i = t.index(cs, i) + 1
    if cnt == len(s):
        return True
    else:
        return False


s, t = "acb", "ahbgdc"
print(isSubsequence(s, t))


def isSubsequenceWhile(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) > len(t):
        return False

    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        return True
    else:
        return False


print(isSubsequenceWhile(s, t))
