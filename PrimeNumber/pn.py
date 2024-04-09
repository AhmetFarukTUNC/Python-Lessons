# Take input from the user
number = int(input("Input number : ")) 

# Assume the number is prime initially
asalMi = "Yes"

# Iterate over numbers from 2 to (number-1)
for x in range(2,number):
    # Check if the number is divisible by x
    if(number%x == 0):
        # If it is divisible, then it's not prime
        asalMi="No"
        # Exit the loop since we found a divisor
        break

# Check if the number is still marked as prime
if asalMi =="Yes":
    # If it is, print that it's a prime number
    print("This number is prime number.")
else:   
    # If it's not marked as prime, print that it's not a prime number
    print("Not prime number.")
