# Set Operations in Python

## This Python script demonstrates the use of set operations, specifically the difference and symmetric difference, using Python sets.

## Difference Operation

### The difference between two sets, denoted by `setA - setB` or `setA.difference(setB)`, returns a set containing elements that are in `setA` but not in `setB`.

## Symmetric Difference Operation

### The symmetric difference between two sets, denoted by `setA ^ setB` or `setA.symmetric_difference(setB)`, returns a set containing elements that are in either `setA` or `setB`, but not in both.

## Code Explanation

### setA = set((1,2,3,4,5))  # Define setA

### setB = set((1,3,4,6,7,8))  # Define setB

# Difference Operation

## print(setA - setB)  # Prints elements of setA that are not in setB

## print(setA.difference(setB))  # Equivalent to the above

# Symmetric Difference Operation

## print(setA ^ setB)  # Prints elements of setA that are different from setB or vice versa

## print(setA.symmetric_difference(setB))  # Equivalent to the above
