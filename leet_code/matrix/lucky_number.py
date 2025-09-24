"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""

def lucky_number(matrix):
    rows, cols = len(matrix), len(matrix[0])
    res = []

    row_min = set()
    for r in range(rows):
        row_min.add(min(matrix[r]))        

    col_max = set()
    for c in range(cols):
        curr_max = matrix[0][c]

        for r in range(rows):
            curr_max= max(curr_max, matrix[r][c])
        col_max.add(curr_max)

    for n in row_min:
        if n in col_max:
            res.append(n)
    return res

print(lucky_number([[3,7,8],[9,11,13],[15,16,17]]))