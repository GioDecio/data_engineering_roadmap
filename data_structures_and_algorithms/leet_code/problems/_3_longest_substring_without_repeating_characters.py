"Given a string s, find the length of the longest substring without duplicate characters."


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    l = 0
    longest = 0
    n = len(s)
    uniques = set()

    for r in range(n):
        print(f"Iter: {r}, char: {s[r]}")
        in_ = 0
        while s[r] in uniques:
            uniques.remove(s[l])
            l += 1
            print(f" while loop iteration number: {in_} ")
            in_ = +1

        w = r - l + 1
        longest = max(longest, w)
        uniques.add(s[r])

    return longest


inputs = ["abcabcbb", "bbbbb", "pwwkew", "pwwkewxpw", "parcazia"]
expected = [3, 1, 3, 5, 5]

results = zip(inputs, expected)

for i, result in enumerate(results):
    if i == 4:
        print(f"Out: {lengthOfLongestSubstring(result[0])} - Exp: {result[1]}")
