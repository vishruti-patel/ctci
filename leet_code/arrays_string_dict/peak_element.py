"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
"""

# #O(n):
# def peak_element(arr):
#     for i in range(len(arr)):
#         if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#             return i
        
# print(peak_element([1,1,3,4,3]))

#O(log(n)) :
def peak_element(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right)//2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

print(peak_element([1,2,1,5,6]))
            