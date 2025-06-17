"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def productExceptSelf(nums):
    output = [1] * len(nums)

    left =1
    for i in range(len(nums)):
        output[i] = output[i] * left
        left = left * nums[i]
    print(output)

    right = 1
    for i in range(len(nums) -1, -1, -1):
        output[i] = output[i] * right
        right = right * nums[i]
    print(output)

    
productExceptSelf([1,2,3,4])