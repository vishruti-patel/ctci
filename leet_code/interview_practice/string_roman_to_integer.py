s = 'IX'
m = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
    
answer = 0

for i in range(len(s)-1):
    if m[s[i]] < m[s[i+1]]:
        answer = m[s[i+1]] - m[s[i]]
        # answer = answer -  m[s[i]]
    else:
        answer = answer + m[s[i]]

answer = answer + m[s[-1]]

print(answer)



"""

len(s) = 3
range(3) --> 0, 1,2
answer = 0

s = III

i = 0, s[0] = I       s[1] = I   --> I<I    --> answer = 0 + 1 = 1

i = 1, s[1] = I =1     s[2] = I   --> I<I    --> answer = 1 + 1 = 2

i= 2, s[2] = I =1                             --> answer = 2+ 1 = 3


"""