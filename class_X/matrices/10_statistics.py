"""

Dema’s classmates ran a 100 m race and recorded these times (in seconds):

13.9 14.3 14.4 13.7 15.2 15.4 13.9 13.9 
14.5 14.7 14.4 13.8 13.1 13.8 12.4 13.8 
12.7 13.4 13.9 14.0 14.4 14.3 14.5 11.8 
12.9 12.3 12.8 13.7 13.1 15.0 14.8 14.2 14.4 14.8 15.2

A. Determine each value:
• the maximum value and minimum value 

• the range
• the median and mean
• the lower and upper quartiles

"""
import numpy as np

data = np.array([13.9,14.3,14.4,13.7,15.2,15.4,13.9,13.9,14.5,14.7,14.4,
                13.8,13.1,13.8,12.4,13.8,12.7,13.4,13.9,14.0,14.4,14.3,
                14.5,11.8,12.9,12.3,12.8,13.7,13.1,15.0,14.8,14.2,14.4,14.8,15.2])



mean = round(np.mean(data),1)

median = round(np.median(data),1)

max_value = round(np.max(data),1)

min_value = round(np.min(data),1)

# ptp() method to calculate range
data_range = round(np.ptp(data),1)

lower_quartile = round(np.quantile(data,0),1)

inter_quartile = round(np.quantile(data,0.5),1)

upper_quartile = round(np.quantile(data, 1),1)

standard_deviation = round(np.std(data),1)

variance = round(np.var(data),1)




print("Mean of the dataset is ",mean)
print("Median of the dataset is ",median)
print("Maximum value in the dataset is ",max_value)
print("Minimum value of the dataset is ",min_value)
print("The range of the datase is ", data_range)
print("Lower quartile of the dataset is ",lower_quartile)
print("Inter quartile of the dataset is ",inter_quartile)
print("Upper quartile of the dataset is ",upper_quartile)
print("The standard deviation of the dataset is ",standard_deviation)
print("The variance of the dataset is ",variance)


