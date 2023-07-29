def matrix_multiplication(mat1, mat2):
    # Find the dimensions of matrices
    m1, n1 = len(mat1), len(mat1[0])
    m2, n2 = len(mat2), len(mat2[0])
    
    # Check if the matrices can be multiplied
    if n1 != m2:
        print("Matrices cannot be multiplied.")
        return
    
    # Initialize a result matrix with zeros
    res = [[0 for _ in range(n2)] for _ in range(m1)]
    
    # Perform multiplication
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                res[i][j] += mat1[i][k] * mat2[k][j]
    
    return res
# Define two matrices
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Multiply the matrices
result = matrix_multiplication(mat1, mat2)

# Print the result
for row in result:
    print(row)
