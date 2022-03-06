"""

Determine the value of a Nu 5000 investment after two years if it is invested at 
an interest rate of 7% p.a. compounded at each frequency:

a) annually b) semi-annually c) quarterly d) monthly e) daily What do you notice?

"""

print("COMPOUND INTEREST CALCULATOR")

principal = float(input("Enter the principal amount Nu."))

rate = float(input("Enter the rate (in decimal) : "))

time = int(input("Enter the time : "))

calculate = "Y"

def calculateAmount(p, r, t, n):

    amount = p * (1 + float(r / n))**( n * t)
    return amount

while calculate == "y":
    n = int(input("Enter 1 for compounded annually:\n Enter 2 for semi-annually \n 4 for quarterly \n 12 for monthly and \n 365 for daily :"))

    if n == 1:
        amountAnnually = calculateAmount(principal, rate, time, 1)
        print("The amount after 2 years compunded annually is Nu.", round(amountAnnually,2))

        calculate = input("Enter Y to coninue :")
    
    elif n == 2 :
        amountSemiannually = calculateAmount(principal, rate, time, 2)
        print("The amount after 2 years compunded semi-annually is Nu.", round(amountSemiannually,2))
        calculate = input("Enter Y to coninue :")
    
    elif n == 4:
        amountQuarterly = calculateAmount(principal, rate, time, 4)
        print("The amount after 2 years compunded quarterly is Nu.", round(amountQuarterly,2))
        

    elif n== 12:
        amountMonthly = calculateAmount(principal, rate, time, 12)
        print("The amount after 2 years compunded monthly is Nu.", round(amountMonthly,2))
        calculate = input("Enter Y to coninue :")
    
    elif n == 365:
        amountDaily = calculateAmount(principal, rate, time, 365)
        print("The amount after 2 years compunded daily is Nu.", round(amountDaily,2))
        calculate = input("Enter Y to coninue :")
    else:
        print("ERROR")
        print("Enter correct frequency correctly")
        print("-----------------------------------")



