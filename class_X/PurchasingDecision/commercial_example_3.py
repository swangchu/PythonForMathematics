"""
Write a program for the given problem

A salesperson had total sales of Nu 60,000.
a) The salesperson is awarded a commission amount of Nu 3000. 
    Determine the rate of commission.

b) Suppose the salesperson is to be paid a rate of commission of 7%. 
    Determine the amount of commission the salesperson would earn.
"""

total_sale = 60000
commission = 3000

# Part a of the problem
commission_rate = ( commission / total_sale ) * 100

print("The rate of commission is ",commission_rate,"%")

#Part b of the question

commission_rate = 0.07

commission_amount = commission_rate * total_sale 

print("The commission amount would be Nu.",commission_amount)
