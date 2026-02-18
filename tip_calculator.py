print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? $"))
tip_percent= int(input("How much tip would you like to give? 10, 12 or 15? "))
people= int(input("How many people to split the bill? "))
total_bill= bill + (bill * tip_percent / 100)
bill_per_person= total_bill / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")