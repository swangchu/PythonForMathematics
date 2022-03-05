"""
Write a python program to solve the given situation below:

A restaurant meal usually costs Nu 80. A special rate of Nu 60 is offered for lunch 
on Thursdays only. Calculate the percent discount.

Get marked price and selling price from the user. And make sure selling price is either equal
or less than the marked otherwise inform the user.
"""

print("***********************************************")

print("Welcome to the discount percentage calculator when marked and selling price are given.")

marked_price = float(input("Enter the marked price Nu."))

selling_price = float(input("Enter the selling price Nu."))

if marked_price >= selling_price :

    discount = marked_price - selling_price

    discount_percent =  ( discount / marked_price ) * 100

    print("The percentage discount was ",discount_percent,"%")

else:

    print("The selling price should be equal or less than the marked price.")
