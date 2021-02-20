#Welcome screen
print("Welcome to the tip calculator!")
#Variables and questions
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#If user says below 10, program calls them cheap and line 5 loops.
while tip < 10:
  print("Why are you so cheap, please give that person a good tip >:(")
  tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
#Calculation
tip_percent = tip / 100
tip_final = bill * tip_percent
bill_final = bill + tip_final
people_final = bill_final / people
grand_total = round(people_final, 2)
#Grand total 
print(f"Each person should pay ${grand_total}")