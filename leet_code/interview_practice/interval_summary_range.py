"""
you are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Input: nums = [0,1,2,4,5,7] 
Output: ["0->2","4->5","7"]

 start = nums[0]
i = 3, --> 4 != 3  -->  start,i-1  -->  [0,2]
if 0 == 0


for i in nums:
if nums[i] != nums[i-1]+ 1:
    return  [start, nums[i-1]]
    start = nums[i]  --> 4

    if start == nums[-1]:
        res.append(str(start))
    else:
        res.append(f"{start}->{nums[-1]}")
    
    return res


"""


def summary_range(nums):
    res = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            if start == nums[-1]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i-1]}")

                start = nums[i]

    if start == nums[len(nums) - 1]:
        res.append(str(start))
    else:
        res.append(f"{start}->{nums[-1]}")

    return res

print(summary_range([0,1,2,4,5,7,9]))


