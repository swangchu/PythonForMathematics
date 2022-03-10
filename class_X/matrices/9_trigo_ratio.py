"""
Mathematic problem

 The legs of a right triangle are 5.0 cm and 8.0 cm. 
 What are the angle measures in the triangle?

"""

import numpy as np

length_opposite = 5

length_base = 8

"""
 tan x = opposite / base
"""
# arctan() is the inverse of tan()

angle_rad = np.arctan(length_opposite / length_base)

angle_deg = round(np.rad2deg(angle_rad))

another_angle = 90 - angle_deg

print("One angle is ",angle_deg,"degree")

print("Another angle is ",another_angle,"degree")
