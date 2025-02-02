

def is_palindrome(input):
    char_count = {}

    for char in input:
        char_count[char] = char_count.get(char, 0) + 1
    print('created dict is:', char_count)

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count = odd_count + 1
    
    if odd_count  <= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_palindrome("abbba"))
    

    
