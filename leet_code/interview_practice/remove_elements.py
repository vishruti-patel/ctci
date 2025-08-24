def remove_element():
    nums = [3,2,2,3,4]
    val = 3
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return nums[:k]

nums = remove_element()
print("New length:", nums)
