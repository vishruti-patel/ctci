def removeDups(arr):

    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
           arr[j] = arr[i]
           j = j +1
    print(arr)


removeDups([1,1,2,2,3])