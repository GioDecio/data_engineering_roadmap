# Ensures strict hierarchy among parentheses is obeyed when there is a nested expression.
# If there is a nested expressions, the bracket squares must be the outmost element,
# followed by square brackets and then round brackets.
# Examples:
# (){}()()()()[] should True
# {[]()} should return False
# {[]((()))} should return False
# {[(())]} should return True
# Even if all the examples above are balanced, in some of them the hierarchy is not obeyed.
# With strict hierarchy we mean that even if you have a nested expression, the difference of the levels in the string,
# and consequewntly in the stack, cannot be greater than 1.
# So this sequence is not valid: "{(", these are: "[(" or "{[".


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
                if (
                    char in parentheses_dictionary
                    and stack[-1] == parentheses_dictionary[char]
                ):
                    if (
                        len(stack) > 1
                        and parentheses_levels[stack[-2]]
                        - parentheses_levels[stack[-1]]
                        > 1
                    ):
                        return False
                    else:
                        stack.pop()
                else:
                    return False
    if not stack:
        return True
    return False


s1 = "(]) Exp: False"
s2 = "}{} Exp: False"
s3 = "[] Exp: True"
s4 = ") Exp: False"
s5 = "[](){} Exp: True"
s6 = "[()] Exp: True"
s7 = "((() Exp: False"
s8 = ")((( Exp: False"
s9 = "[](){} Exp: True"
s10 = "({}) Exp: False"
s11 = "{[()]} Exp: True"
s12 = "(){}()()()()[] Exp: True"
s13 = "{[(())]} Exp: True"
s14 = "{[]()} Exp: False"  ### <----
s15 = "[]((()))(){} Exp: True"
s16 = "{[]((()))} Exp: False"
s17 = "{((()))} Exp: False"
s18 = "{()[]} Exp: False"
s19 = "{}}{()()((((((())))))) Exp: False"
s20 = "{[(())]} Exp: True"
s21 = "{()]} Exp: False"
s22 = "{[()]()} Exp: False"
s23 = "{[([])]} Exp: False"

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
    s18,
    s19,
    s20,
    s21,
    s22,
    s23,
]

cardinal = [i for i in range(1, len(input_list) + 1)]

input_dict = dict(zip(cardinal, input_list))

for i, in_string in enumerate(input_dict):
    if i > 0:
        print(
            f"{i} - Exp: {input_list[i-1].split(' ')[-1]} -",
            f"R: {is_valid(input_list[i-1].split(' ')[0])}",
        )
