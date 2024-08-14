import numpy as np

def determinant(matrix):
  n = len(matrix)
  
  # Base case: If the matrix is 1x1, return the single element
  if n == 1:
    return matrix[0][0]
  
  # Base case: If the matrix is 2x2, compute determinant directly
  if n == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  
  det = 0
  
  # Choose a row or column to expand the determinant
  for j in range(n):
    # Compute the cofactor for element matrix[0][j]
    sign = (-1) ** j
    cofactor = sign * matrix[0][j] * determinant(submatrix(matrix, 0, j))
    # Add the cofactor to the determinant
    det += cofactor
  
  return det

def submatrix(matrix, row_exclude, col_exclude):
  n = len(matrix)
  submat = [[0 for _ in range(n-1)] for _ in range(n-1)]
  row_index = 0
  for i in range(n):
    if i == row_exclude:
      continue
    col_index = 0
    for j in range(n):
      if j == col_exclude:
        continue
      submat[row_index][col_index] = matrix[i][j]
      col_index += 1
    row_index += 1
  return submat

matrix = np.array([
 [  5,  10,  -8,   1,  -9,   4,   2,   3,   6,   7,   0,  -3,  -6,  -2,   9,  -1],
 [ -3,   0,   6,  -5,   2,   3,  -1,  -7,   4,  -4,   1,   9,  -2,  -8,  -6,   5],
 [ -6,  -7,   9,  -8,   4,   2,  -4,   0,   5,   1,   7,  -3,  -1,   3,  -9,   6],
 [  1,   9,   0,   3,  -8,  -2,   7,   5,  -6,  -4,   2,  -5,   8,  -3,   6,  -1],
 [ -4,   8,   5,  -3,  -1,   0,  -9,  -6,   2,  -7,   4,   1,  -8,   9,   3,  -2],
 [ -2,  -1,  -6,   4,   7,   9,  -8,   1,   3,   6,  -5,  -4,  -3,   0,   8,  -7],
 [  7,   3,   4,  -6,   0,  -5,  -1,   8,  -9,  -2,  -7,   2,   6,   1,  -4,   9],
 [ -9,   5,  -2,   7,   1,  -6,  -3,   2,  -4,   0,   8,   3,  -5,  -1,   6,  -8],
 [  6,  -4,  -1,  -9,  -3,  -8,   5,  -7,   0,   9,  -6,   7,   4,   2,  -5,   1],
 [ -8,  -2,   7,   2,   6,   1,   4,   9,  -5,  -3,   0,  -9,   3,  -6,   5,  -4],
 [ -5,   6,   3,   8,  -2,  -7,   0,  -4,   1,   5,  -9,   6,  -1,   7,  -8,   2],
 [ -1,   7,  -9,   6,  -4,   5,  -2,   3,  -8,  -1,   3,  -8,   0,  -4,   7,  -6],
 [ -7,   1,   8,  -4,   5,  -3,   6,  -9,   2,   4,  -1,   0,   9,  -5,  -2,   3],
 [ -3,  -5,  -4,   0,  -6,   8,   1,   4,  -7,  -8,   5,   7,  -2,   6,  -1,   9],
 [  0,  -9,   1,   5,   3,   6,  -7,  -2,   8,   4,  -1,  -6,  -4,  -8,   7,  -3],
 [  9,   2,  -3,  -7,  -5,   7,   3,  -1,  -4,   8,  -2,   4,   1,   5,  -8,   0]
 ]
)
rank = np.linalg.matrix_rank(matrix)

# normalize the matrix

matrix = matrix / np.linalg.norm(matrix)

# compute the transpose of the matrix

matrix = matrix.T

# find the eigenvalues of the matrix and print them

eigenvalues = np.linalg.eig(matrix)

#compute the rank of the matrix

rank = np.linalg.matrix_rank(matrix)

# expand the matrix to 32 x 32

matrix = np.pad(matrix, ((0, 16), (0, 16)), 'constant')

# fill in the zeroes of the matrix with random numbers

matrix = np.random.rand(32, 32)

rank = np.linalg.matrix_rank(matrix)
print(rank)

# compute the determinant of the matrix using np

det = np.linalg.det(matrix)
print(det)
