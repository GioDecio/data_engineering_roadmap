def palindrome_checker(s):

    if len(s) % 2 == 0:
        return "This string can't be palndrome"
    right_idx = len(s) - 1
    for idx, char in enumerate(s):
        print(f"The right end is {s[right_idx]}")
        print(f"right_idx id {right_idx}")
        if idx == right_idx:
            break
        if char != s[right_idx]:
            return False
        right_idx -= 1

    return True


s = "deified"
check = palindrome_checker(s)
print(check)
