"""
Write a python program to solve the given situation below:

A restaurant meal usually costs Nu 80. A special rate of Nu 60 is offered for lunch 
on Thursdays only. Calculate the percent discount.
"""

marked_price = 80

selling_price = 60

discount = marked_price - selling_price

discount_percent =  ( discount / marked_price ) * 100

print("The percentage discount was ",discount_percent,"%")
