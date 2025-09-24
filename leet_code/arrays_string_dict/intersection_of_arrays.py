"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""


def intersection(num1, num2):
    res = []
    for i in range(len(num1)):
        if num1[i] in num2 and num1[i] not in res:
            # if num1[i] not in res:
                res.append(num1[i])

    return res

print(intersection([4,9,5,2], [9,4,5,8]))