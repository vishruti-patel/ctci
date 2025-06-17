def reverse_vowels_in_string(string):
    vowels = "aeiouAEIOU"
    rev_string = []

    vow = [char for char in string if char in vowels]
    print(vow)

    for c in string:
        if c in vowels:
            rev_string.append(vow.pop())
        else:
            rev_string.append(c)
    print(''.join(rev_string))
    

reverse_vowels_in_string("icecream")
reverse_vowels_in_string("rIchiE")