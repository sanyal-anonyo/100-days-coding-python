print("Welcome to the tip Calculator!")
bill_amount = float(input("What was the total bill? $"))

tip_percent = float(input("How much tip would you like to give? 10, 12 or 15?"))

head_count = int(input("How many people to split the bill?"))

each_part_bill = (bill_amount + (bill_amount * tip_percent / 100))/head_count

print(f"Each person should pay:", each_part_bill)