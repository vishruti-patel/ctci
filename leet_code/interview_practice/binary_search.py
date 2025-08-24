
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity
"""


def binary_search(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
       mid = (left + right)//2

       if target > nums[mid]:
           left = mid + 1
       elif target < nums[mid]:
           right = mid -1
       else:
           return mid
       
    return left

print(binary_search([1,2,3,5,7,8,9], 6))
