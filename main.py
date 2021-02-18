#Welcome screen
print("Welcome to the tip calculator!")
#Variables and questions
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
#Converting variables into floats and ints
bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)
#Calculation
tip_percent = tip_int / 100
tip_final = bill_float * tip_percent
bill_final = bill_float + tip_final
people_final = bill_final / people_int
grand_total = round(people_final, 2)
#Grand total 
print(f"Each person should pay ${grand_total}")