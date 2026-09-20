# MathCore-PK | Linear Algebra Toolkit
# For BS Mathematics Students - Peshawar
import numpy as np

def matrix_operations():
    print("Linear Algebra - Matrix Example")
    A = np.array([[1, 2], [3, 4]])
    print("Matrix A:\n", A)
    print("Determinant:", np.linalg.det(A))
    print("Inverse:\n", np.linalg.inv(A))

if __name__ == "__main__":
    matrix_operations()
