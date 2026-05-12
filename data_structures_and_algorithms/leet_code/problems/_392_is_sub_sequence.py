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
    if len(s) > len(t):
        return False

    cnt = 0
    i = 0
    for cs in s:
        if cs in t[i:]:
            cnt += 1
            i = t.index(cs, i) + 1
    return cnt == len(s)


def isSubsequenceWhile(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


from functools import lru_cache


def isSubsequenceRecursion(s, t):
    def dp(i, j):
        if i == len(s):
            return True
        if j == len(t):
            return False
        if s[i] == t[j]:
            return dp(i + 1, j + 1)
        else:
            return dp(i, j + 1)

    return dp(0, 0)


def isSubsequenceMemo(s, t):

    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s):
            result = True
        elif j == len(t):
            result = False
        elif s[i] == t[j]:
            result = dp(i + 1, j + 1)
        else:
            result = dp(i, j + 1)

        memo[(i, j)] = result
        return result

    return dp(0, 0)


s, t = "acb", "ahbgdc"
print(isSubsequence(s, t))
print(isSubsequenceWhile(s, t))
print(isSubsequenceRecursion(s, t))
print(isSubsequenceMemo(s, t))
