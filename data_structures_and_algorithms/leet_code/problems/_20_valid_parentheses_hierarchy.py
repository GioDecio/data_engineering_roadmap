# Ensures hierarchy among parentheses is obeyed when there is a nested expression.
# If there is a nested expressions, the bracket squares must be the outmost element,
# followed by square brackets and then round brackets.
# Examples:
# (){}()()()()[] should True
# {[]()} should return True
# {[]((()))} should return True
# {[(())]} should return True
# In all the examples above prentheses are balanced.
# With not strict hierarchy we mean that when you have a nested expression, the difference of the levels in the string,
# and consequently in the stack, can be greater than 1.
# So these sequences are valid: "{(", "[(" or "{[".


def is_valid(s):

    stack = []
    parentheses_dictionary = {")": "(", "]": "[", "}": "{"}
    parentheses_levels = {"{": 3, "[": 2, "(": 1}

    for i, char in enumerate(s):
        if char in parentheses_dictionary.values():
            if not stack or parentheses_levels[char] <= parentheses_levels[stack[-1]]:
                stack.append(char)
            else:
                return False
        else:
            if not stack:
                return False
            else:
                if stack[-1] == parentheses_dictionary[char]:
                    stack.pop()
                else:
                    return False
    if not stack:
        return True
    return False


s1 = "(])"
s2 = "}{}"
s3 = "[]"
s4 = ")"
s5 = "[](){}"
s6 = "[()]"
s7 = "((()"
s8 = ")((("
s9 = "[](){}"
s10 = "({})"
s11 = "{[()]}"
s12 = "(){}()()()()[]"
s13 = "{[(())]}"
s14 = "{[]()()}"
s15 = "[]((()))(){}"
s16 = "{[]((()))}"
s17 = "{((()))}"

input_list = [
    s1,
    s2,
    s3,
    s4,
    s5,
    s6,
    s7,
    s8,
    s9,
    s10,
    s11,
    s12,
    s13,
    s14,
    s15,
    s16,
    s17,
]

for i, input_string in enumerate(input_list):
    print(i + 1, is_valid(input_string))
