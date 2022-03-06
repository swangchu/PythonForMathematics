"""
    Karma borrowed Nu 20,000. He repaid the loan at the end of 4 years with a single payment of Nu 35,680. 
    What interest rate was charged, if the compounding was semi-annual?

"""
print("RATE CALCULATOR")

principal = 20000

amount = 35680

time = 4

n = 2


rate = (( amount/principal)**(1/ (n * time))- 1) * n 

rate_percent = round(rate,2) * 100

print("The interest rate charged was Nu.", rate_percent,"%")
