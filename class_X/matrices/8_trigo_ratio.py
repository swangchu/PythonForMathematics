"""
Mathematic problem

 A ladder leaning against a wall forms a 25° angle with the wall at the top of the ladder. 
 If the ladder reaches 2.8 m up the wall, how long is the ladder?

"""

import numpy as np

# height in meter
height = 2.8

angle_in_rad = np.deg2rad(25)

ladder = height / np.sin(angle_in_rad)

print("The lenght of ladder is ",round(ladder,1),"m")
