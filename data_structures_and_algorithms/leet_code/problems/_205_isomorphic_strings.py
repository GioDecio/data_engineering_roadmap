def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool

    """

    if len(s) != len(t):
        return False

    char_dict = {}
    values = set()

    for char_s, char_t in zip(s, t):
        if char_s in char_dict and char_dict[char_s] != char_t:
            return False
        elif char_t in values and char_s not in char_dict:
            return False
        else:
            char_dict[char_s] = char_t
            values.add(char_t)

    return True


inputs = [("paper", "title"), ("badc", "baba"), ("egg", "add"), ("foo", "bar")]

for pair in inputs:
    print(pair)
    print(isIsomorphic(pair[0], pair[1]))
