"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


*STACK* -> whenever puzzle is to match pairs

"""


def is_valid(s):
    stack = []
    h_map = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in s:
        if char in h_map.values():
            stack.append()

        elif char in h_map.keys():
            if not stack or h_map[char] != stack.pop():
                return False
            
    return not stack


print(is_valid(["([])"]))
