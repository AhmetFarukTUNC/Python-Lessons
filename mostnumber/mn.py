number1 = int(input("Number 1 : ")) # We take a number from user assign to number1 variable.

number2 = int(input("Number 2 : ")) # We take a number from user assign to number2 variable.

number3 = int(input("Number 3 : ")) # We take a number from user assign to number3 variable.

# If number1 greater than number2 and number3,then,we assigned number1 to biggestNumber.

if (number1 >= number2) and number1 >= number3:
   biggestNumber = number1

# If number2 greater than number1 and number3,then,we assigned number2 to biggestNumber.

if (number2 >= number1) and number2 >= number3:
   biggestNumber = number2

# If number3 greater than number1 and number2,then,we assigned number3 to biggestNumber.

if (number3 >= number1) and number3 >= number2:
   biggestNumber = number3

print("Biggest Number :",biggestNumber) # We printed biggestNumber variable.