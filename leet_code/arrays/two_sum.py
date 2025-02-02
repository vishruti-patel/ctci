"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

eg: input = [2,3,7,11]
    target = 9
    OUTPUT:  [0,2]

d = {}  
arr = []

d = {index: value for index, value in enumerate(arr)}

"""


# def two_numbers():
# arr = [2,3,7,11]
# new_arr = list(arr)
# target = 9

# def two_numbers(arr):
#     target = 9
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] + arr[j] == target:
#                 return i, j

# if __name__ == "__main__":
#     print(two_numbers([2,3,4,7]))


#using hash:
nums = [2,7,22,25]
val = 9

d = {key: index for index, key in enumerate(nums)}
for i in d.keys():
    ans = val - i
    if ans in d:
        print(d[ans])
    