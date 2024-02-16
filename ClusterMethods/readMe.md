# Set Methods in Python

## Introduction

### Sets in Python are unordered collections of unique elements. They are commonly used for mathematical 

### operations like union, intersection, difference, and symmetric difference. 

# This README provides an overview of the methods available for sets in Python.

## Set Methods

## 1. add()

### Syntax: set.add(element)

### Adds a single element to the set. If the element is already present, the set remains unchanged.

## 2. clear()

### Syntax: set.clear()

### Removes all elements from the set, leaving it empty.

## 3. copy()

### Syntax: set.copy()

### Returns a shallow copy of the set.

## 4. difference()

### Syntax: set1.difference(set2)

### Returns a new set containing elements that are present in set1 but not in set2.

## 5. remove()  

### Syntax: set.discard(element)

### Removes the specified element from the set if it is present.

## 6. intersection()

### Syntax: set1.intersection(set2)

### Returns a new set containing elements that are present in both set1 and set2.

## 7. isdisjoint()

### Syntax: set1.isdisjoint(set2)
### Returns True if set1 and set2 have no elements in common, otherwise returns False.

## 8. issubset()

### Syntax: set1.issubset(set2)
### Returns True if set1 is a subset of set2, otherwise returns False.

## 9. issuperset()

### Syntax: set1.issuperset(set2)
### Returns True if set1 is a superset of set2, otherwise returns False.

## 10. pop()

### Syntax: set.pop()
### Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

## 11. remove()

### Syntax: set.remove(element)
### Removes the specified element from the set. Raises a KeyError if the element is not present.

## 12. symmetric_difference()

### Syntax: set1.symmetric_difference(set2)
### Returns a new set containing elements that are present in either set1 or set2, but not in both.

## 13. union()

### Syntax: set1.union(set2)
### Returns a new set containing all unique elements present in either set1 or set2.

## 14. update()

## Syntax: set1.update(set2)
## Modifies set1 to include all elements from set2.

# Conclusion

## This document provides a comprehensive overview of the methods available for sets in Python. These methods allow for efficient manipulation and operations on sets, making them a valuable tool for various programming tasks.

# What Is The Superset?

## A superset is a set that contains all the elements of another set, including the other set itself.In

## other words, if set A contains all the elements of set B and possibly more, then set A is considered a 

## superset of set B.Mathematically, if A and B are sets, and every element of B is also an element of A, 

## then A is said to be a superset of B, denoted as A ⊇ B.In Python, you can determine if a set is a 

## superset of another set using the issuperset() method or the >= operator.

## set1 = {1, 2, 3, 4, 5}

## set2 = {1, 2, 3}

## # Using the issuperset() method

## print(set1.issuperset(set2))  # Output: True

## # Using the >= operator

## print(set1 >= set2)  # Output: True

## In this example, set1 is a superset of set2 because all the elements of set2 (1, 2, and 3) are also 

## present in set1. Additionally, set1 contains more elements than set2. Therefore, set1 is considered a 

## superset of set2.


























