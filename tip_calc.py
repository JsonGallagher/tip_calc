print("Welcome to the tip calculator ")
#Get bill total
total_bill = float(input("What was the total bill? $"))

#Get tip, calc new bill total
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_plus_tip = total_bill + (total_bill * (percent_tip / 100))

#Get number of guests splitting bill
split = int(input("How many people to split the bill? "))
bill_per_person = (bill_plus_tip / split)
bill_per_person = round(bill_per_person, 2) #round 2 decimal places

#Display bill per person
print(f"Each person should pay: ${bill_per_person}")