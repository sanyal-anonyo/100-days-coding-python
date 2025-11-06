print("Welcome to Atreyee's Pizza Deliveries!")

size = input("What size of Pizza do you want? S, M, or L: ")
pepperoni = input("Do you want Pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    price = 375
elif size == "M":
    price = 450
elif size == "L":
    price = 575
else:
    price=0

if pepperoni == "Y":
    price=price+127
if extra_cheese == "Y":
    price=price+69

print("Your final cost is going to be INR",price)
