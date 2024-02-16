number = int(input("Please,input your number : "))

control = (number > 0) and (number%2==1)

if control == True:
    print("{} is positive single number.".format(number))

else:
    print("{} is not positive single number.".format(number))