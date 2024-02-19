number = int(input("Please,input your number : ")) # We took a number from user

control = (number > 0) and (number%2==1) # It assigns 0 or 1 according to result.If number is greater than 

# 0 and modulus divide to 2 of number is 1,it assigns to 1,othervise assigns to 0.

# If control is 1(True),computer print number,after that,print "is positive single number.".

if control == True:

    print("{} is positive single number.".format(number))

# Otherwise,computer print number,after that,print "is not positive single number.".

else:

    print("{} is not positive single number.".format(number))