"""
    Is Unique: Implement an algorithm to determine if a string has all unique characters. 
    
    What if "you cannot use additional data structures"? 
    Hints: #44, #7 7 7, #732

    input:
        s = "Vishruti"
        ans = False

        s = "Raxit"
        ans = True


        [R, a, x, i, t]

        i = R, a
        j = (i+1) --> x, i, t

        
        sol1: 

        O(n^2)
        for i in range(len(input)):
            for j in range(i+1, len(input)):
                if input[i] == input[j]:
                    return False
        return True                    

        sol2: O(n)

        remember ascii: a=97


        input= [r, a, r, x, i, t]
        char_set = [false for i in range(0, 127)]
        
        for i in range(len(input)):
            ord_i = ord(input[i])
            if char_set[ord_i] == True:
                return False
            else:
                char_set[ord_i] = True

        sol3: O(n)
        input= [r, a, r, x, i, t]
        freq_map = {}
        for char in input:
            if char in freq_map:
                return False
            else:
                freq_map[char] = True
        return True


        char = r,a,r    
        freq_map {r:True, a: True,  }

"""


def is_unique(input):
    char_set = [False] * 128
    for char in input:
        v = ord(char)   #v=97
        if char_set[v] == True:
            return False
        else:
            char_set[v] = True
    return True 

        # print(char)
        # if arr[char] == False:



# will creat an array of 128 chars. [False, False, False]
# Need a for loop that iterates over each char of input string. 
# For each char of string, it will take the ascii value of that char. 
# That ascii value is the index in the array. 
# THat index position will be converted to True.
# another char in string -> go to array -> if index position in char set is True --> return False

# For instance ascii a = 97, it will go to array, look for 97






    # freq_map = {}
    # for char in input:
    #     if char in freq_map:
    #         return False
    #     else:
    #         freq_map[char] = 'present'
    # return True





if __name__ == '__main__':
    input = "raxit"
    print(is_unique(input))
    



