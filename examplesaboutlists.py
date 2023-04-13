# First Example

# Create a list and element of this list bmv,mercedes,opel,mazda

list=["bmw","opel","mercedes","mazda"]

print(list) # ["bmw","opel","mercedes","mazda"]

# How many has  element in the above list?

print(len(list)) # Output is 4.

# print to screen last element and first element in the list

print(list[0]) # It gives first element in the list

print(list[3]) # It gives last element in the list

print(list[-1]) # It gives last element in the list

# change mazda value with toyota in the list.

list[3] = "toyota" # list = ['bmw', 'opel', 'mercedes', 'toyota']

print(list) # ['bmw', 'opel', 'mercedes', 'toyota']

# Is mercedes value in the list?

if "mercedes" in list: # We will explain in the future topic but it means "is mercedes value in the list?"

    print("Mercedes is in the list.") # It prints "Mercedes is in the list".

# Find value of -2.index in the defined previous list

print(list[-2]) # It gives mercedes.

# Take first 3 elements and print to screen.

print(list[0:3])

print(list[:3])

# Add toyota and renault instead of the last 2 variables.

list[2] = "toyota" # list = ['bmw', 'opel', 'toyota', 'mazda']

list[3] = "renault" # list = ['bmw', 'opel', 'toyota', 'renault']

print(list) # list = ['bmw', 'opel', 'toyota', 'renault']

# Add audi and nissan value to the end.

list.append("audi") # list = ['bmw', 'opel', 'toyota', 'renault','audi']

list.append("nissan") # list = ['bmw', 'opel', 'toyota', 'renault','audi','nissan']

print(list) # ['bmw', 'opel', 'toyota', 'renault','audi','nissan']

# Delete last element of list

del list[-1] # list = ['bmw', 'opel', 'toyota', 'renault', 'audi']

print(list) # ['bmw', 'opel', 'toyota', 'renault', 'audi']

# Print all elements from reverse.

print(list[::-1]) # ['audi', 'renault', 'toyota', 'opel', 'bmw']

# 3 list but those is list in list examples.

studentA=["John","KENNEDY",2010,[70,60,90]]

studentB=["Jennifer","LOPEZ",1999,[80,80,70]]

studentC=["Selena","GOMEZ",1998,[80,70,90]]

# Print the list above

print(f"{studentA[0]} {studentA[1]} is {studentA[2]} years old and he is a student with an average of  {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}") # John KENNEDY is 2010 years old and he is a student with an average of  73.33333333333333

print(f"{studentB[0]} {studentB[1]} is {studentB[2]} years old and he is a student with an average of {(studentB[3][0]+studentB[3][1]+studentB[3][2])/3}.") # Jennifer LOPEZ is 1999 years old and he is a student with an average of 76.66666666666667.

print(f"{studentC[0]} {studentC[1]} is {studentC[2]} years old and he is a student with an average of {(studentC[3][0]+studentC[3][1]+studentC[3][2])/3}.") # Selena GOMEZ is 1998 years old and he is a student with an average of 80.0.











