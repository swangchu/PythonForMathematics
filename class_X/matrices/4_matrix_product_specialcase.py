"""
Matrix Multiplication of corresponding elements

*****************************************

Two matrices can be multiplied if the number of columns in the first matrix equals the number of rows in the second matrix.
When comparing dimensions of matrices to see if they can be multiplied, the two inner numbers must match.

For example:
You can multiply 4 × 1 and 1 × 3 matrices, but not 4 × 1 and 2 × 3 matrices.


Lets multiply two matrices

        Matrix A               Matrix B

        |2  1   0|          |10  3   0.5|
        |4  3   2|          |-2  1   -4 |

"""
import numpy as np

A = np.array(
             [(2,  1,   0),
              (4,  3,   2)]
            )

B = np.array(
             [(10,  3,   0.5),
              (-2,  1,   -4)]
            )

# Lets check whether matrices A and B have same shape

if A.shape == B.shape :
    print("Matrices A and B have same shape", A.shape)


# If we use * operator then the corresponding elements in the
# matrices will be multiplied 
# It will not follow standard matrix multiplication 

special_productAB = A * B
print("The product of corresponding elements in Matrix A and B is \n", special_productAB)

# Check whether they are commutative
special_productBA = B * A
print("The product of corresponding elements in Matrix A and B is \n", special_productBA)

#Use the == operator to compare two NumPy arrays to generate a new array object. 
# Call ndarray.all() with the new array object as ndarray to return True if the two NumPy arrays are equivalent.
is_equal = special_productAB == special_productBA
if is_equal.all():
  print("Commutative")
