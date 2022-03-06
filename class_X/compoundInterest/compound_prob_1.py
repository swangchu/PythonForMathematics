"""

Determine the value of a Nu 5000 investment after two years if it is invested at 
an interest rate of 7% p.a. compounded at each frequency:

a) annually b) semi-annually c) quarterly d) monthly e) daily What do you notice?

"""

print("COMPOUND INTEREST CALCULATOR")

principal = 5000

rate = 0.07

time = 2 

# n is the number of interest period in a year
# for annually n is 1
n = 1
def calculateAmount(p, r, t, n):

    amount = p * (1 + float(r / n))**( n * t)
    return amount

amountAnnually = calculateAmount(principal, rate, time, 1)

print("The amount after 2 years compunded annually is Nu.", round(amountAnnually,2))

# n is the number of interest period in a year
# for semi-annually n is 2
amountSemiannually = calculateAmount(principal, rate, time, 2)

print("The amount after 2 years compunded semi-annually is Nu.", round(amountSemiannually,2))

# n is the number of interest period in a year
# for quarterly n is 2
amountQuarterly = calculateAmount(principal, rate, time, 4)

print("The amount after 2 years compunded quarterly is Nu.", round(amountQuarterly,2))

# n is the number of interest period in a year
# for monthly n is 12
amountMonthly = calculateAmount(principal, rate, time, 12)

print("The amount after 2 years compunded monthly is Nu.", round(amountMonthly,2))


# n is the number of interest period in a year
# for daily n is 265
amountDaily = calculateAmount(principal, rate, time, 365)

print("The amount after 2 years compunded daily is Nu.", round(amountDaily,2))

