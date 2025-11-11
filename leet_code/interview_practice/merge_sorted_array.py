# def main():
#     m = 3
#     nums1 = [1,2,3,0,0,0]

#     for i in range(m, len(nums1)):
#         print(f"i = {i}, i-m = {i-m}")

# if __name__ == "__main__":
#     main()



nums1 = [1,2,3,0,0]
nums2 = [2,5,6]


m = 3
n = 3

i = 0
j = 0

while i<m and j<n:
    if nums1[i] <= nums2 [j]:
        i += 1
    else:
        temp = nums1[i]
        nums1[i] = nums2[j]
        nums2[j] = temp

        j += 1

