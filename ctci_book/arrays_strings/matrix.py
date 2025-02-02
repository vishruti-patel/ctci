# matrix = [[column for column in range(4)] for row in range(4)]

# mat = [[1,2], [3,4], [5,6]]
# print(mat)
# flat_mat = [i for row in mat[:2] for i in row]
# print(flat_mat)


#create matrix
matrix = [[column for column in range(4)] for row in range(4)]
print(matrix)

#add a value to specific position/index
row = 1
column = 2
matrix[row][column] = 18
print(matrix)
"""
expression for in a[start:stop] if condition
a = [2,3,4,5,6]
#list comprehension
new_result = [i*2 for i in a[:2]]
print(new_result)

#slicing from end
end_slice = [i for i in a[-2:]]
print("slice from end", end_slice)

#square of every alternate element
alt = [i**2 for i in a[::2]]
print("square of every alternate element", alt)
"""