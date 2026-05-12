def is_valid(s):

    stack = []

    parentheses_dictionary = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                # if (
                #     (char == ")" and stack[-1] == "(")
                #     or (char == "]" and stack[-1] == "[")
                #     or (char == "}" and stack[-1] == "{")
                # ):
                if stack[-1] == parentheses_dictionary[char]:
                    stack.pop()
                else:
                    return False

    if not stack:
        return True
    return False


s1 = "(])"
s2 = "}{}"
s3 = "][]"
s4 = ")"
s5 = ""
s6 = "[()]"
s7 = "((()"
s8 = ")((("
s9 = "[]))))"
s10 = "({})"

print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))
print(is_valid(s5))
print(is_valid(s6))
print(is_valid(s7))
print(is_valid(s8))
print(is_valid(s9))
print(is_valid(s10))
