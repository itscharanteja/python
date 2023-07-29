def add_matrices(matrix1, matrix2):
    """
    Performs addition of two square matrices.
    
    Args:
    matrix1 (list): The first matrix.
    matrix2 (list): The second matrix.
    
    Returns:
    list: The result of the addition.
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Check if matrices have same dimensions
    if len(matrix2) != rows or len(matrix2[0]) != cols:
        raise ValueError("Matrices must have same dimensions")
    
    # Create result matrix with zeros
    result = [[0 for j in range(cols)] for i in range(rows)]
    
    # Add matrices element-wise
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result


# Example usage
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = add_matrices(matrix1, matrix2)
print(result)  # Output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
