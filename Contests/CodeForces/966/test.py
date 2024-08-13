import numpy as np

def times_cell_passed_over(M, N, m, n, i, j):
    row_coverage = min(i, M - m + 1) - max(1, i - m + 1) + 1
    col_coverage = min(j, N - n + 1) - max(1, j - n + 1) + 1
    return row_coverage * col_coverage

# Define matrix and submatrix dimensions
M, N = 9, 5  # Original matrix dimensions
m, n = 3, 3  # Submatrix dimensions

# Create a 9x5 matrix to store the results
result_matrix = np.zeros((M, N), dtype=int)

# Calculate for each cell
for i in range(1, M+1):
    for j in range(1, N+1):
        result_matrix[i-1, j-1] = times_cell_passed_over(M, N, m, n, i, j)

# Print the result
print("Number of times each cell is passed over by a 5x5 submatrix:")
print(result_matrix)
