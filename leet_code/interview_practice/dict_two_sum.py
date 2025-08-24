
nums = [2,3,8,5,7]
tar = 9

new_dict = { }

for i in range(len(nums)):
    val = tar - nums[i]

    if val in new_dict:
        print(new_dict[val], i)

    new_dict[nums[i]] = i



# for n in range(len(nums)):
#     new_dict[nums[n]] = n

# for key, val in 

# print(new_dict)





"""
Brute Force approach

nums = [2,3,8,5,7]
tar = 9


for i in range(len(nums) - 1):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == tar:
            print(i,j)

"""