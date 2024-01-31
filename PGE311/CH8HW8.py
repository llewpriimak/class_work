import numpy as np


def matmult(matrix_x, matrix_y):

    if len(matrix_x[0]) != len(matrix_y):
        return 'THIS IS AN ERROR'
    new_matrix = np.array([])
    for i in range(len(matrix_x)):
        for j in range(len(matrix_y[0])):
            sum_it = 0
            for k in range(len(matrix_y)):
                sum_it += matrix_x[i][k] * matrix_y[k][j]
            new_matrix = np.append(new_matrix, [sum_it])

    final_matrix = np.reshape(new_matrix, (len(matrix_x), len(matrix_y[0])))
    print(final_matrix)

array1 = np.array([[1, 2], [3, 2], [4, 2]])
array2 = np.array([[3, 4, 5], [2, 1, 3]])
bad_array = ([1,2,3,4,5,6,7,9], [2,3,1,5,6,9,-1], [2,4,5,1,0,0,5,1])


matmult(array1,array2)

def rowperm(A, r1, r2):
    """
rowperm: switches rows of matrix A by
multiplying by a permutation matrix
PA = rowperm(A,r1,r2)
input:
A = original matrix
r1, r2 = rows to be switched
output:
PA = matrix A with rows r1 and r2 switches
"""
    identity_m = np.identity(len(A))
    temp = np.copy(identity_m[r1, :])
    identity_m[r1, :] = identity_m[r2, :]
    identity_m[r2, :] = temp

    return (np.matmul(identity_m, A))

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rowperm(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0, 2)
