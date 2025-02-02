def if_equal_char(s):
    freq_count = {}
    for char in s:
        freq_count[char] = freq_count.get(char, 0)+1
    
    tmp_val = freq_count[s[0]]
    for val in freq_count.values():
        if val != tmp_val:
            return False
    return True



print(if_equal_char("abbac"))