"""
Textbook definition of matrix:
-----------------------------------------------------------
A matrix (plural is matrices) is a rectangular 
array of items used to store and display information.
-----------------------------------------------------------

Lets implement the matrix given below in python using NumPy

            |4 3 1 0|
       A =  |7 3 1 8|
            |5 9 1 4|


"""


import numpy as np

# According to definition a matrix is an array
# We have created array for the matrix using NumPy array() method

A = np.array([(4, 3, 1, 0),
              (7, 3, 1, 8),
              (5, 9, 1, 4)]
            )  

# shape  attribute is used to get the shape/ of the matrix
shape_of_A = A.shape

# Shape of the matrix is displayed as (numberOfrows, numberOfcolumns)
# We call it as shape instead of dimentsion in NumPy
print("The dimension of the matrix A is ",shape_of_A)

# if you want number of rows and columns seperately 

row, col = A.shape
print("Number of row in matrix A is ",row)
print("Number of columns in matrix A is ",col)

# size atribute displays the number of element in a matrix
number_of_elements_A = A.size
print("The number of elements in matrix A is ",number_of_elements_A)

# Access an element of a matrix using indexing
# NumPy follows zero indexing meaning counting starts from 0
# The element 9 is at 3rd row which is 2 and 2nd column which is 1
element_9 = A[2, 1]
print("Element at 3rd row and 2nd column in the matrix is ",element_9)

# Access all elements in a row
# A[row,] keep the column part empty
first_row = A[0,]
print("Elements of the First row in marix A are ",first_row)

# Another way
# : mean all the columns
first_row = A[0,:]
print("Elements of the First row in marix A are ",first_row)

# Access all elements of a column in matrix
# Unlike accessing all elements of a row, we cant keep row blank in accessing a column
# 0:3 means from 0th row till 2nd row, 3 is excluded

first_column = A[0:3 , 0]
print("All elements of the first column of a matrix A is",first_column)

# Another way to access the elements in a row
second_column = A[ :, 2]
print("All elements of the second column of a matrix A is",second_column)


# Finally to display all the elements 
# You just have to call the matrix name
print("Matrix A = \n",A)


"""
-----------------------------
Concepts covered
-----------------------------
1. creating a matrix 
2. Shape attribute
3. Size attribute
4. Accessing a element
5. Accessing a row
6. Accessing a column
7. Slice
8. Zero indexing
9. Access a matrix
"""