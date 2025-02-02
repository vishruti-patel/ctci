""" Given two strings, write a method to decide if one is a permutation of the 
    other.
"""

#soln: both strings same char and same length
# s1 = "abc"
# arr = list(s1)
# print(arr)
# print(type(arr))

# a = ['s,a']
# print(a)
# print(type(a))


s1 = "riche"
s2 = "rihe"

new_s1 = sorted(s1)
print(new_s1)
new_s2 = sorted(s2)
if new_s1 == new_s2:
    print("yes")
else:
    print("No")



# def perm_string():
#      if new_s1 == new_s2:
#          print("yes")
#      else:
#           print("No")


# print(new_s1)

# if len(s1) == len(s2):
#     print("may be")

# else:
#     print("No chance")

"""

def string_rotation(string1, string2):
    d = {}
    for char in string1:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1

    for char in string2:
        if char in d:
            d[char] = d[char] - 1
        else:
            return False
        
    for val in d.values():
        if val > 0:
            return False

    return True
        # d[char] = d.get(char, 0)+1

if __name__ == '__main__':
    print(string_rotation("pasta", "stapa"))

"""


