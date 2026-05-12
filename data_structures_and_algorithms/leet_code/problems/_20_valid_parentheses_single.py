def is_valid(s):

    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if char != ")":
                return False
            elif not stack:
                return False
            else:
                stack.pop()

    if not stack:
        return True

    return False


s1 = "(]"
s2 = "()"
s3 = "((((("
s4 = ")"
s5 = ""
s6 = ")("
s7 = "((()"
s8 = ")((("
s9 = "())))"

print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))
print(is_valid(s5))
print(is_valid(s6))
print(is_valid(s7))
print(is_valid(s8))
print(is_valid(s9))
