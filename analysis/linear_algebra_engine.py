import numpy as np


def matrix_operations():

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    B = np.array([
        [5, 6],
        [7, 8]
    ])

    multiplication = np.dot(A, B)

    transpose_A = A.T

    determinant_A = np.linalg.det(A)

    inverse_A = np.linalg.inv(A)

    return multiplication, transpose_A, determinant_A, inverse_A