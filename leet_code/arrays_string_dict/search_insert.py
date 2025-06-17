def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left<=right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left
        

print(search_insert([1,2,4,5,6,7], 6))