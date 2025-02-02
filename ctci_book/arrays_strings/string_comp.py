def compression(string):
    result_string = ""
    count = 1
    for char in range(1, len(string)):
        # print(char-1, string[char-1])
        #if string[char] == string [char + 1]
        if string[char] == string[char - 1]: 
            # print(string[char], string[char-1]) 
            count += 1
        else:
            # print(string[char], string[char-1]) 
            result_string += string[char-1] + str(count)
            count = 1             
    #     # if string[char] == string[char+1]:
    result_string += string[char] + str(count)
    return result_string

print(compression("aabbbccc"))




"""
a,b,b -> 1,2,3
char[1] --> char[0]

"""

# def compression(input):

#     ct = 0
#     for char in input:



# if __name__ == '__main__':
#     print(compression())


# string = "aabb"
# for char in range(len(string)):
#         if string[char] == string[char + 1]:
#             print(string[char])