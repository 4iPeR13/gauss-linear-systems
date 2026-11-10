# def gauss(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     A = [row[:] for row in matrix]
#     cur_row = 0
#     free_variables = []
#     pivot_cols = []

#     for col in range(n):
#         pivot_row = -1
#         for row in range(cur_row, m):
#             if A[row][col] == 1:
#                 pivot_row = row
#                 break
#         if pivot_row == -1:
#             free_variables.append(col)
#             continue

#         A[cur_row], A[pivot_row] = A[pivot_row], A[cur_row]
#         pivot_cols.append(col)

#         for row in range(m):
#             if row != cur_row and A[row][col] == 1:
#                 A[row] = [(A[row][i] ^ A[cur_row][i]) for i in range(n)]

#         cur_row += 1
import numpy as np
def gauss(matrix):
    m = len(matrix)
    n = len(matrix[0]) - 1 

    A = [row[:] for row in matrix]

    # Прямий хід
    for i in range(min(m, n)):
        max_row = max(range(i, m), key=lambda r: abs(A[r][i]))
        if abs(A[max_row][i]) < 1e-12:
            continue 
        A[i], A[max_row] = A[max_row], A[i]

        factor = A[i][i]
        A[i] = [a / factor for a in A[i]]
        
        for j in range(i + 1, m):
            factor = A[j][i]
            A[j] = [A[j][k] - factor * A[i][k] for k in range(n + 1)]

        print(f"\nКрок {i+1}:")
        for row in A:
            print(" ".join(f"{val:.6f}" for val in row))
    # Зворотний хід
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] - sum(A[i][j] * x[j] for j in range(i + 1, n))

    return x
A = [
    [3.81, 0.25, 1.28, 0.75],
    [2.25, 1.32, 4.58, 0.49],
    [5.31, 6.28, 0.98, 1.04],
    [9.39, 2.45, 3.35, 2.38]
]

b = [4.21, 6.47, 2.38, 10.48]

matrix = [A[i] + [b[i]] for i in range(len(A))]

solution = gauss(matrix)


print("Розв'язок:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
    
A_matrix = np.array(A)
b_vector = np.array(b)
x_vector = np.array(solution)
residual = np.abs(b_vector - A_matrix @ x_vector)

print("\nВектор нев’язки:")
for i, val in enumerate(residual):
    print(f"r{i+1} = {val:.6e}")