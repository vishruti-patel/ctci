str = 'VII'

def roman_to_integer():
    roman_dict = { 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ans = 0

    for i in range(len(str) - 1):
        if roman_dict[str[i]] < roman_dict[str[(i+1)]]:
            ans = ans - roman_dict[str[i]]
        else:
            ans = ans + roman_dict[str[i]]
            
        # print(ans)

    return ans + roman_dict[str[-1]]

if __name__ == '__main__':
    ans = roman_to_integer()
    print(ans)


    



