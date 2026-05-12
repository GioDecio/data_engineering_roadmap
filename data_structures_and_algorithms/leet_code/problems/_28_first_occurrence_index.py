# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# Prep ex:

# ---
# Esercizio 1
# Scrivi una funzione che prende una stringa s e un intero i, e restituisce una sottostringa di s che inizia all'indice i e ha lunghezza 3.

# # Esempio:
# # s = "sadbutsad", i = 0  →  "sad"
# # s = "sadbutsad", i = 3  →  "but"
# # s = "sadbutsad", i = 6  →  "sad"


def subString(s, i):
    return s[i : i + 3]


# Esercizio 2:
#  ---
# Ora generalizza: scrivi una funzione che restituisce la sottostringa di s che inizia all'indice i e ha la stessa lunghezza di una stringa needle.
def subStringGen(s, needle, i):
    return s[i : i + len(needle)]


# Esercizio 3:
# ---
# Scrivi una funzione che itera su tutti gli indici validi di haystack da cui
# potresti estrarre una sottostringa di lunghezza len(needle). Stampa ogni indice.


# # Esempio: haystack = "sadbutsad", needle = "sad"
# # Output: 0, 1, 2, 3, 4, 5, 6
def subStringIdx(haystack, needle):
    n = len(haystack) - len(needle) + 1
    for i in range(len(haystack[:n])):
        print(i)


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    n = (
        len(haystack) - len(needle) + 1
    )  # Number of valid starting positions for the sliding window
    for i in range(len(haystack[:n])):  # Define range of index
        if (
            haystack[i : i + len(needle)] == needle
        ):  # compare sub string with the needle
            return i

    return -1
