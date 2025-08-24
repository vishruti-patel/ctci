def binarySearch(arr, target):

    left = 0
    right = len(arr) - 1

    while left<=right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    return left
        

print(binarySearch([1,2,4,5], 3))