"""
    .One Away: There are three types of edits that can be performed on strings: insert a character, 
    remove a character, or replace a character. Given two strings, write a function to check if they are 
    one edit (or zero edits) away.

    EXAMPLE 
    pale, ple -> true 
    pales, pale -> true 
    pale, bale -> true 
    pale, bake -> false

    ----

    abcde acd

    1. we can modify only 1 character inside string
    
    pale, 
    ple

    p == p -> true
    a == l -> false 
        if l(i1) != l(i2):
            input[i] + inp ut[i:]

    i, j = 0, 0

    ip[i] != ip2[j]:
        # remve char
        # add
        # replace
        # input[i:] == input2[j:]

        return False
"""

"""
def is_one_edit_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    
    i, j = 1, 0
    edits = 0
    while i < len(string1) and j < len(string2):
        # char1, char2 = input1[i], input2[j]

        if edits >= 1:
            return False
        
        if string[i] != string[j]: 
            edits += 1           
            # insert
            if len(string1) != len(string2):
               if string2[j] + string1[i:] == string2[j:]:
                   return True
               
               if string1[i] + string2[j:] == string1[i:]:
                   return True
            
            # Todo://
            # replace
            # remove
        i += 1
        j += 1
    
    # return False
    


if __name__ == '__main__':
    input1, input2 = "pale", "bale"
    print(is_one_edit_away(input1, input2))
"""


def is_one_edit_away(string1, string2):
    if string1 == string2:
        return True

    if abs(len(string1) - len(string2)) > 1:
        return False
    
    i = 0
    j = 0
    edit_count = 0
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            edit_count += 1

            if edit_count > 1:
                return False
            
            if len(string1) < len(string2):
                j = j+1
            elif len(string1) > len(string2):
                i = i+1
            else:
                i = i+1
                j = j+1
        else:
            i = i+1
            j = j+1
    return True

if __name__ == '__main__':
    print(is_one_edit_away("hei", "hei"))