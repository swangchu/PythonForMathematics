"""
Matrix Multiplcation with a scalar

*****************************************

You can multiply a matrix by a single value, called a scalar.
To do this, you multiply each element in the matrix by that value.

Lets multiply a matrix with a scalar

    |1 2|           
A=  |3 4|        
    |5 6|

"""
import numpy as np

A = np.array([(1,2),
              (3,4),
              (5,6)]
            )


# Scalar product of a matrix
scalarProduct = 10 * A
print("Scalar product of matrix A is \n", scalarProduct)

# Lets see the data type of the matrix A
# dtype attribute describing the type of the elements in the array.
type_of_A = A.dtype
print("The matrix A contains ",type_of_A,"data types")

# min() method returns the minimum element in the matrix A
min_element = A.min()
print("The minimum element in matrix A is ", min_element)

# max() method returns the maximum element in the matrix A
max_element =A.max()
print("The maximum element in matrix A is ",max_element)

"""
concepts covered
++++++++++++++++++++++

1. scalar product
2. dtype attribute
3. min() method
4. max() method

"""