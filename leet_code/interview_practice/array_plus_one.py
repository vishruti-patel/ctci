"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.


--Approach: Reverse traversal and carry propgation. 

run a for loop in the reversr order to check if the last digit is < 9. If it is just add 1 and return.
Edge case is what if [9,9]. In that case we just add [1] + digits which will give [1,0,0]
"""


def plus_one(digits):
    for i in reversed(range(len(digits))):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        
        digits[i] = 0

    return [1] + digits

print(plus_one([1,2,3,4]))
print(plus_one([9,9]))