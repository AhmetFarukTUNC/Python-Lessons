# Prime Number Checker

## This Python script checks whether a given input number is a prime number or not.

## Usage

### 1. Run the script.

### 2. Input a number when prompted.

### 3. The script will determine whether the input number is prime or not and print the result.

## How it Works


### # Take input from the user

#### number = int(input("Input number : ")) 

### # Assume the number is prime initially

#### asalMi = "Yes"

### # Iterate over numbers from 2 to (number-1)

#### for x in range(2,number):

#### # Check if the number is divisible by x

#### if(number%x == 0):

####  # If it is divisible, then it's not prime

####       asalMi="No"

####  # Exit the loop since we found a divisor

####       break

### # Check if the number is still marked as prime

####   if asalMi =="Yes":

####     # If it is, print that it's a prime number

####       print("This number is prime number.")

####   else:   

####      # If it's not marked as prime, print that it's not a prime number

####      print("Not prime number.")

## Explanation

###  The script takes a number as input from the user.

#### It then checks whether the number is divisible by any integer between 2 and the number itself minus 1(including 2 and number itself minus 1 but not including number).

#### If the number is divisible by any of these integers, it's not prime.

#### If the number is not divisible by any of these integers, it's prime.

#### The script prints the result accordingly.