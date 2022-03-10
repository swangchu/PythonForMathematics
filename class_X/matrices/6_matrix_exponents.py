"""
Matrix Multiplcation

*****************************************

Lets multiply two matrices

    |1 2|           |7  8   9|
A=  |3 4|        B= |10 11 12|
    |5 6|

A**2 * B

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
# product of A square and B

product_AB = A**2 @ B
print("Product of matrix A and B is \n",product_AB)

