"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


s = ' hey baby '  #op= 'baby hey'
reversed_s = []
words = s.split()

for i in range(len(words) -1, -1, -1):
    reversed_s.append(words[i])
print(reversed_s)

reversed_s = ' '.join(reversed_s)
print(reversed_s)