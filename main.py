#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill = input("How much was your total bill? $")
amountOfPeople = input("How many people are splitting the bill?")
desiredTipAmount = input("How much would you like to to tip? 10%, 15%, 20%?")

amountWithoutTip = float(bill)/float(amountOfPeople)

amountPerPerson = amountWithoutTip +(amountWithoutTip * (float(desiredTipAmount)/100))

print(f"Each person should pay ${round(amountPerPerson, 2)} ")