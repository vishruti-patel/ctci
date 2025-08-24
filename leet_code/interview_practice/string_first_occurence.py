# haystack = 'hebirhheyhiiiee'
# needle = 'hey'

# # print(haystack[6:9], haystack[0:3], haystack[5:8])
# # if haystack[0:3] == needle:
# #     print('True')

# if len(haystack) < len(needle):
#     print(-1)

# for i in range(len(haystack)):
#     if haystack[i : i + len(needle)] == needle:
#         print(i)

# print(-1)

def first_occurence(haystack, needle):
    # haystack = "abcde"
    # needle = "ec"

    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        if haystack[i: i+len(needle)] == needle:
            return i
        
    return -1

if __name__ == '__main__':
    print(first_occurence('acbcd', 'cd'))
    




# d = { }

# using for loop to iterate and create dictionary
# for key, val in enumerate(needle):
#     d[val] = key

# d = {val: key for key , val in enumerate(needle)}
# print(d)


"""
haystack = 'Lagunabeach'
needle = 'beach'


[10:41] 

for char in haystack:
    if char == needle[0]:
        for i in 


        







d ={'b' : 0,
    'e' : 1,
    'a' : 2,
    'c' : 3,
    'h' : 4
    }

i = 0
for char in haystack:  
    if char == needle[i]:
        i += 1
    

L == b
a == b, g == b, u ==b, n ==b, a == b, 
b == b  --> i =1

e == e --> i =2
 
a == a  --> i = 3

c == c --> i = 1

h == h 


   




"""

