"""
Write a program for the given problem

A salesperson had total sales of Nu 60,000.
a) The salesperson is awarded a commission amount of Nu 3000. 
    Determine the rate of commission.

b) Suppose the salesperson is to be paid a rate of commission of 7%. 
    Determine the amount of commission the salesperson would earn.
"""

total_sale = float(input("Enter the total sales Nu."))
commission = float(input("Enter the comission amount Nu."))

# Part a of the problem
commission_rate = ( commission / total_sale ) * 100

print("The rate of commission is ",commission_rate,"%")

#Part b of the question
print("--------------------------------------------------------------")
print("Part B of the question")

commission_rate = float(input("Enter the commission rate in decimal"))

commission_amount = commission_rate * total_sale 

print("The commission amount would be Nu.",commission_amount)
