# How can I use format method

# Format method is a function like print function so It is printing to screen the text.It has a lot of parameters.Number of parameter is depending to number of word in {}. 

name = "Jonathon"

print("My name is {}".format(name)) 

#Here,curly brace is equal value of name variable so computer is printing "My name is Jonathon" string expression.

# Different structures for use format function

#First structure format function

surname = "Delph."

print("My name is {} {}".format(name,surname)) 

#Here,first curly braces is equal value of name variable and second curly braces is equal value of surname variable so computer is printing "My name is Jonathon Delph." string expression.

# Second structure for format function

print("My name is {0} {1}".format(name,surname)) 

#Output is equal "My name is Jonathan Delph." string expression.

# Third Structure for format function

# Print value of surname variable before value of name variable

print("My name is {1} {0}".format(name,surname))#Output is equal "My name is Delph. Jonathan" string expression.

#Forth structure for format function

#We assigned to n name and we assigned to s surname.Output is equal "My name is Jonathan Delph." string expression.

print("My name is {n} {s}".format(n=name,s=surname))

#Different a example but important!!!

result = 200/700 #It is equal to 0.2857142857142857.

#We assigned to r result on the bottom line and {r} is equal to value of result.Finally,output is equal "The result is 0.2857142857142857." string expression.

print("The result is : {r}.".format(r=result))


#Computer is taking 0 as whole area and computer takes four number after that(,) so output is equal "The result is 0.2857." string expression.({r:0(whole area).4(for takes four number after comma(,)))

print("The result is : {r:0.4}.".format(r=result))

# We defined name surname.But We need age variable.

age=18

# Fifth structure for format function

# We are adding f letter to the top and we are filling necessary place with correct variable.

#Here,Output is equal to "My name is Jonathan({name}) Delph({surname}).I am 18({age}) years old."

print(f"My name is {name} {surname}I am {age} years old.")

# Sample questions

website = "http://w.w.w.merhaba.com"

course = "0 to expert python tutorial"

# How much has course variable character?

print("Length is {}".format(len(course)))

#find "w.w.w." text in website variable and print to screen.

print(website[7:13])

# take ".com" text in the website variable and print to screen.

print(website[20:24]) # on the top

print(website[len(website)-4:len(website)])# on the bottom

# Take 15 character on the top and bottom

# Execute on the bottom line for take 15 character on the top.

# Execute this for take 15 character on the top.

print(course[0:15]) # or print(course[:15]) 

print(course[:15])

# Execute this for take 15 character on the bottom

print(course[-15:])

# print from reverse all characters in the course expression.

print(course[ : :-1])

# A different example

password = "12345"*5

print(password[::5]) #Output is 11111

# Second example

name,surname,age,job = "Angelina","Jolie",34,"Actress"

print("My name is "+ name + " " + surname + ".I am " + str(age) + " years old.I am " + job + ".")# Output is "My name is Angelina Jolie.I am 34 years old.I am actress."

print("My name is {} {}.I am {} years old.I am {}.".format(name,surname,age,job))# Output is "My name is Angelina Jolie.I am 34 years old.I am actress."

print("My name is {0} {1}.I am {2} years old.I am {3}.".format(name,surname,age,job))# Output is "My name is Angelina Jolie.I am 34 years old.I am actress."

print(f"My name is {name} {surname}.I am {age} years old.I am {job}.")# Output is "My name is Angelina Jolie.I am 34 years old.I am actress."

# Change with W w letter of "Hello world".

sentence = "Hello world!"

# First Way

sentence=sentence[0:6] + "W" +sentence[-5:] 

print(sentence) # Output is "Hello World!"

# Second Way

sentence = "Hello world!"

# Replace is replacing second parameter with first parameter in default variable.Default variable is value that you defined on the top.

print(sentence.replace("w","W")) # Output is Hello World!

# New Example

# Print three times to side by side "abc" expression.

expression = "abc\n" * 3 # You can continue from bottom line with \n.

print(expression) 

# Output is on the bottom.

# abc

# abc

# abc




