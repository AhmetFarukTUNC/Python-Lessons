multiplication = 1 # multiplication variable value is 1.This is initial value.

numbers = range(1,100) # We took 1 to 100 numbers and assigned to numbers variable.

# We assigned to multiplication variable each value in numbers as multiplication.

for i in numbers:
    multiplication *= i

# We printed to multiplication value.

print(multiplication)