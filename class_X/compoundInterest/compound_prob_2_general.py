"""
    Karma borrowed Nu 20,000. He repaid the loan at the end of 4 years with a single payment of Nu 35,680. 
    What interest rate was charged, if the compounding was semi-annual?

"""
print("RATE CALCULATOR")

principal = float(input("Enter the principal amount Nu."))

amount = float(input("Enter the amount Nu."))

time = float(input("Enter the loan period (years)"))

n = int(input("Enter the interest period: "))


rate = (( amount/principal)**(1/ (n * time))- 1) * n 

rate_percent = round(rate,2) * 100

print("The interest rate charged was Nu.", rate_percent,"%")
