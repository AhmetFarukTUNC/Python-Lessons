number1 = int(input("Number 1 : "))

number2 = int(input("Number 2 : "))

number3 = int(input("Number 3 : "))

if (number1 >= number2) and number1 >= number3:
   biggestNumber = number1

if (number2 >= number1) and number2 >= number3:
   biggestNumber = number2

if (number3 >= number1) and number3 >= number2:
   biggestNumber = number3

print("En Büyük :",biggestNumber)