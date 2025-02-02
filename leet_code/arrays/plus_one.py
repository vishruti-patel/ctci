
"""


"""

# for i in reversed(digit):
#     if i < 9:
#         i += 1
#         print(i)
#     else:
#         i = 0

def plus_one(digit):
    for i in range(len(digit) -1, -1, -1):
        if digit[i] < 9:
            digit[i] += 1
            return digit
        else:
            digit[i] = 0
    return [1] + digit              #for the scenario when digit = [9]

print(plus_one([9,9,9]))


    



