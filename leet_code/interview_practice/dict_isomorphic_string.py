"""Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""


def isomorphic(s,t):
    s_map = {}
    t_map = {}

    for s_char, t_char in zip(s,t):
        if s_char in s_map and s_map[s_char] != t_char:
            return False
        if t_char in t_map and t_map[t_char] != s_char:
            return False
        s_map[s_char] = t_char
        t_map[t_char] = s_char

    return True
    
print(isomorphic('paper', 'title'))
        

# def isomorphic(s, t):
#     if len(s) != len(t):
#         return False
    
#     map = { }

#     for i in range(len(t)):
#         if t[i] not in map:
#             map[t[i]] = s[i]
#         elif t[i] in map:
#             if map[t[i]] == s[i]:
#                 continue
#         else:
#             False
# print(isomorphic('paper', 'titlt'))
