"""
Matrix Addition and Subtraction
++++++++++++++++&&&-------------

• You can add or subtract matrices that have numerical elements, but the matrices must have the same dimensions.
• When you add or subtract matrices, you find the sum of, or difference between, the elements in the same positions in the matrices.

Lets add and subtract two matrices

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
    print("Matrices A and B can be added or subtracted since they have same shape")


# Add the two matrices
add_matrix_AB = A + B
print("A + B is \n",add_matrix_AB)

print("------------------------------------")

# Subtract A from B
sub_matrix_AB = B - A
print("B - A is \n",sub_matrix_AB)

# Subtract B from A
sub_matrix_BA = A - B
print("A - B is \n",sub_matrix_BA)