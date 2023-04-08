# First Example

name = "Chiristian" # or name = 'Chiristian'

surname = "George"  #or surname = 'George'

age=36

print("My name is " + name + " " + surname)

# Second example

name = " George"

surname = " Bush"

deneme = "My name is"

print( deneme + name + surname )

# This is Third Example and about str and int additional error.

name = "Christian "

surname = "Swift."

age=36

# print("My name is " + name + surname + ".I am " + age +" years old.")

#For fix the error you can change age of data type as str.You can do str to int convert.Also we defined to name,surname and age variable name.

print("My name is " + name + surname + "I am " + str(age) +" years old.")

# This is fourth example.This example about bring index of any string expression.Also we defined to name,surname and age variable name.I won't define this variables.

greeting = "My name is " + name + surname + "I am " + str(age) + " years old."

print(greeting)

print(greeting[0])

print(greeting[3])

print(greeting[len(greeting)-1])

# This is fifth example.This example about bring index of any string expression and take lenght of greeting expression.Also we defined to name,surname,age and greeting variable name.I won't define this variables.

length=len(greeting)

print(length)

print(greeting[length - 1]) # Last character

print(greeting[-1]) # Last character

print(greeting[2:5]) # output is space and first two letter of name word.

print(greeting[3:]) # Output is "name is Chiristian Swift.I am 36 years old" string expression without first space.

print(greeting[:15]) # Output is "My name is Chiri" string expression without first space.

print(greeting[2:40:2]) # First area is start index and Second area is one more than last index.Last area is number of step so output is  "aei hita wf. m3 er" string expression.
