def replace_char_string(input):
    new_s = list(input)
    print(new_s)
    
    for char in range(len(new_s)):
        if new_s[char] == " ":
            new_s[char] = "%20"
            print("".join(new_s))
if __name__ == '__main__':
    replace_char_string("vi patel")


#using built-in function
# s1=s.replace(" ", "%20")
# print(s1)
        

# arr =['v','i','p','a','t']
# arr_to_string = "".join(arr)
# print(arr_to_string)
