print("Welcome to the roller coaster!")
height = int(input("Please enter your height in cms: "))
age = int(input("Please enter your age: "))

if height >120:
    if age > 18:
        print("You can ride the rollercoaster and the ticket will cost $12")
    else:
        print("You can ride the rollercoaster and the ticket will cost $7")

else:
    print("Sorry you have to grow taller before you can ride.")

