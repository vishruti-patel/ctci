"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

def two_strings():
    ransomeNote = "hey"
    magazine = "how are you"

    d = {}


    for char in magazine:
        d[char] = 1 + d.get(char, 0)

    for ch in ransomeNote:
        if ch not in d:
            return False
               
    return True

    # print(d)

print(two_strings())






