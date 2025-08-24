"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


def is_duplicate(nums, k):
    d = { }

    for i in range(len(nums)):
        if nums[i] in d and abs(i - d[nums[i]]) <= k:
            return True
        d[nums[i]] = i

    return False

print(is_duplicate([1,2,3,1], 3))