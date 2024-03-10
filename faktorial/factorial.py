number = int(input("Number = ")) # We took a number from user.

fac = 1 # fac is equal to 1.

# If number is lesser than 0,then,print "Doesnt calculate factorial of negotive number."

if number < 0:
    print("Doesn't calculate factorial of negotive number")

# If number is equal to 0,then,print "Result is 1."

elif number == 0:
    print("Result is 1.")

# Otherwise,print value of factorial.

else:
    for i in range(1,number + 1):
        fac = fac*i

    print(fac)
