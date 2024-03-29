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
