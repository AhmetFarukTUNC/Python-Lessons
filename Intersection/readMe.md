# Set Intersection Operations

## This repository contains Python code demonstrating how to perform intersection operations on sets.

## Contents

### 1. [Introduction](#introduction)

### 2. [Usage](#usage)

### 3. [Code Explanation](#code-explanation)

## Introduction

### Sets in Python are unordered collections of unique elements. One of the common operations performed on 

### sets is the intersection, which returns the common elements between two sets.

### This repository includes a Python script that defines two sets (`setA` and `setB`) and demonstrates 

### how to perform the intersection operation using both the `&` operator and the `intersection()` method.

## Usage

### To use this code, follow these steps:

### 1. Clone this repository to your local machine:

#### git clone https://github.com/AhmetFarukTUNC/Python-Lessons

### 2. Navigate to the repository directory:

#### cd Desktop/Python-Lessons/Intersection


### 3. Run the Python script:

#### python si.py


### 4. View the output in the terminal, which will display the result of the intersection operations 

### between `setA` and `setB`.

## Code Explanation

### The Python script (`si.py`) contains the following code:

#### setA = set((1,2,3,4,5)) # Define setA

#### setB = set((1,3,4,6,7,8)) # Define setB

# Perform intersection operation using '&' operator

#### print(setA & setB)

# Perform intersection operation using intersection() method

#### print(setA.intersection(setB))

### setA and setB are defined using the set() constructor, with tuples containing elements.

### The intersection operation is performed using both the & operator and the intersection() method.

### The results of the intersection operations are printed to the console.

## Feel free to explore the code and modify it as needed for your own projects!