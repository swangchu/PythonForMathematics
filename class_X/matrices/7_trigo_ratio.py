"""
Mathematics Problems
+++++++++++++++++++++++++++++++++++++++++++++++++++
Vishnu leaned a 10 m ladder against a building at an angle of 70°. 
How high up the building does the ladder go?

"""
import numpy as np

hypotenuse = 10

"""
sin(70) = opposite / hypotenuse

"""
# deg2rad() converts degree to radian
rad = np.deg2rad(70)

# The trogonometric ratios takes in radian that is why we have converted 
# degree to radian
height = np.sin(rad) * hypotenuse

print("The ladder will go ",np.round(height,1),"m from the ground")


"""
concepts covered

1. deg2rad() method
2. sin() ration
3. round() method

"""