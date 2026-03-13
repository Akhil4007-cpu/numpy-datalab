import numpy as np

def matrix_operations():

    # create two random matrices
    A = np.random.rand(3,3)
    B = np.random.rand(3,3)

    print("\nMatrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    # matrix multiplication
    multiplication = np.dot(A, B)

    # transpose
    transpose_A = A.T

    # determinant
    determinant_A = np.linalg.det(A)

    # inverse
    inverse_A = np.linalg.inv(A)

    return multiplication, transpose_A, determinant_A, inverse_A