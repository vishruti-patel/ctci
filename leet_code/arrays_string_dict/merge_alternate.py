"""
#Leetcode 75
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

s1 = "abcdj"
s2 = "pqr"
string = []

for char1,char2 in zip(s1,s2):
    string.append(char1 + char2)
    # string = string+ list(char1) + list(char2)    #another way to concates strings
print(string)

string.append(s1[len(s2):])
string.append(s2[len(s1):])
print(''.join(string))


# for c1 in s1:
#     for c2 in s2:
#         s = s +c1 + c2
# print(s)m
# for c1,c2 in zip(s1,s2):
#     s.append(c1+c2)

# s.append(s1[len(s2):])
# s.append(s2[len(s1):])
# s = ''.join(s)
# print(s)

# s.append(s1[len(s2):])
# s.append()

