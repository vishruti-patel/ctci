"""
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""

def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    print(rows, cols)

    res = [[0] * rows for _ in range(cols)]

    for r in range(rows):
          for c in range(cols):
               res[c][r] = matrix[r][c]
    return res

print(transpose([[1,2,3],[4,5,6]]))