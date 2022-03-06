"""
Dawa invests Nu 125,000 in RICB shares with a face value of Nu 100 but are being sold at a premium of 25%. 
How many shares can Dawa buy?
"""
print("SHARE CALCULATOR")

investment = float(input("Enter the amount of investment to buy share Nu."))

face_value = float(input("Face value of a share Nu."))

premium_percent = float(input("Enter the premium :")) 

market_value = face_value + ( premium_percent / 100) * face_value

total_share = investment / market_value

print("Dawa can buy ",round(total_share,2),"shares for the investment of Nu.",round(investment,2),"at the market value of Nu.",round(market_value,2))
