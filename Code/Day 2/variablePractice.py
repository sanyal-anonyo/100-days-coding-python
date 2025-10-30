#subscripting
print("Hello"[0])

print("Hello"[-1])

print("Hello"[4])

#string
print("123"+"456")

#integer = whole number

print(123+456)

#large integers

print(123_456_789)

#float = floating point numbers

print(3.145)

#Boolean
print(True)
print(False)

#len method

print(len("Hello"))
print(type("Hello"))
print(type(123))
print(type(123.45))
print(type(True))

#casting

print(int("123")+int("456"))

name_of_the_user = input("Enter your name:")
length_of_name = len(name_of_the_user)

print(type("Length of you name is "))#str
print(type(length_of_name))

print("Length of you name is " + str(name_of_the_user))

#mathematical operator

print("my age: "+str(12))
print(1+2)
print(1-2)
print(1*2)
print(5/3)
print(5//3)


height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height**2)

print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2))