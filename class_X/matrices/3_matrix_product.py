"""
Matrix Multiplcation

*****************************************

Two matrices can be multiplied if the number of columns in the first matrix equals the number of rows in the second matrix.
When comparing dimensions of matrices to see if they can be multiplied, the two inner numbers must match.

For example:
You can multiply 4 × 1 and 1 × 3 matrices, but not 4 × 1 and 2 × 3 matrices.

Lets multiply two matrices

    |1 2|           |7  8   9|
A=  |3 4|        B= |10 11 12|
    |5 6|

"""
import numpy as np

A = np.array([(1,2),
              (3,4),
              (5,6)]
            )

B = np.array([(7,8,9),
              (10,11,12)]
            )

#lets check whether these matrices can be multiplied
# Just checking the condition for matrix multiplication

rowA, colA = A.shape
rowB, colB = B.shape

if colA == rowB:
    print("Matrices A and B can be multiplied")


# since the shape of A and B is not same 
# we use @ operator for standard matrix multiplication 

product_AB = A @ B
print("Product of matrix A and B is \n",product_AB)

print("********************************************")
# Another method 
# use .dot() operator to multiply two matrices

product_AB = A.dot(B)
print("Product of matrix A and B using .dot() is \n",product_AB)

# Let see if matrix multiplication is commutative

product_BA = B.dot(A)
print("Product of matrix A and B using .dot() is \n",product_BA)

# Matrix multiplication is not commutative
