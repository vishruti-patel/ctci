def remove_ele(arr, val):
    k =0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k]= arr[i]
            k = k+1
    print("count is", k)
  
    
remove_ele([1,2,1,2,3,1], 3)


#what if I want to return new array?