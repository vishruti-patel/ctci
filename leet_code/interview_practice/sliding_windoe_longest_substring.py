"""
Given a string s, find the length of the longest substring without duplicate characters.
"""
def longest_subaraay(s):
    left = 0
    char_set = set()
    string_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        string_length =  max(string_length, right - left + 1)

    return string_length


print(longest_subaraay('ababbb'))
            




 

