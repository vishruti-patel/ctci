def majority_element(nums):
    freq = {}
    n = len(nums)
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    element = n // 2
    print(element)

    for key, val in freq.items():
        if val > element:
            return key

print(majority_element([1,2,2,2,2,1,1]))