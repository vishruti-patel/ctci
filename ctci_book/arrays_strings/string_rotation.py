"""
    Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring 
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one 
call to i5Sub5tring (e.g., "waterbottle" is a rotation of"erbottlewat").

pasta
astap/ stapa/  apast
apast


"""

def string_rotation(string1, string2):
    if len(string1) != len(string2):
        return False

    if string2 not in string1+string1:
        return False

    return True

if __name__ == '__main__':
    print(string_rotation("pasta", "stapa"))




