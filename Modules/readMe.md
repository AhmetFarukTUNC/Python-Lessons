# Simple Calculator

## This is a simple Python script containing functions for summing and multiplying two numbers, as well as a dictionary example.

## Functions

### `summazation(number1, number2)`

#### This function takes two numbers as input and prints their sum.


### def summazation(number1, number2):
###    print("Sum: " + str(number1 + number2))

### multiplication(number1, number2)

#### This function takes two numbers as input and prints their multiplication result.



### def multiplication(number1, number2):

###    print("Result: " + str(number1 * number2))

## Example Usage

### Summation
#### summazation(5, 3)  # Output: Sum: 8

# Multiplication
#### multiplication(5, 3)  # Output: Result: 15

# Customer Dictionary

## We defined a dictionary named customer, which contains the first name and last name of a customer.


### customer = {
### "firstName": "Ahmet Faruk",
### "lastName": "TUNC"
### }

## Usage

### You can use these functions in your Python scripts by importing them and calling them with appropriate arguments.

### from module import summazation, multiplication

# Use the functions

## summazation(5, 3)
## multiplication(5, 3)

## Feel free to modify and integrate these functions into your projects as needed.

# Module Integration Example

## This is a simple Python script demonstrating the integration of functions from a module.

## Description

### The script imports a custom module containing functions for summation and multiplication, as well as a dictionary. It then demonstrates how to use these functions and access the dictionary values.

## Usage

### To use this script, follow the steps below:

#### 1. Ensure you have the `module.py` file in the same directory as your script.
#### 2. Import the necessary functions or variables from the module using `import` or `from ... import`.
#### 3. Call the imported functions or access the imported variables as needed.

## Example Usage


### # Importing the module
### import module

### # Printing the sum of numbers 2 and 3
### module.summazation(2, 3)

### # Multiplying 3 and 4 and printing the result
### module.multiplication(3, 4)

### # Printing the value of the 'firstName' key in the 'customer' dictionary
### print(module.customer["firstName"])

### # Importing the 'summazation' function from the module
### from module import summazation

### # Adding 3 and 5 numbers and printing the result
### summazation(3, 5)

### # Accessing the 'customer' dictionary directly
### from module import customer
### print(customer)
