print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip would ou like to give? 10, 12 or 15? "))
attendants = int(input("How many people to split the bill? "))

tip = (bill * (1+percentage/100))/attendants

print(f"Each Person should pay: ${round(tip,2)}" )