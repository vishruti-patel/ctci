"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

# nums = [1, 0, -1,1,2,-3]

# for i in range(len(nums) - 2):
#     if nums[i] + nums[i+1] + nums[i+2] == 0:
#         print(nums[i],nums[i+1],nums[i+2])

#     else:
#         continue


def three_sum():
    nums = [-2,-2,0,1,3,-1,2]
    arr =[]
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i+1
        k = len(nums) - 1

        while j<k:
            total = nums[i] + nums[j]+nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                arr.append([nums[i], nums[j], nums[k]])
                j += 1

                while j < k and nums[j] == nums[j-1]:
                    j +=1 

        
    print(arr)

            # while nums[j] == nums[j-1] and j < k:
            #     j += 1


if __name__ == '__main__':
    three_sum()