# Upper : It prints big all letters.

message = " Hello There.My name is Johnson Cat."

print(message.upper())

# Lower : It prints small all letters.

print(message.lower())

# Title : It prints big first letter for every word.

print(message.title())

# Capitalize : It only prints big  first letters.

print(message.capitalize())

# Strip : It deletes space on the top.

print(message.strip())

#Split  : It is seperating according to space and this element assigns to a array.

print(message.split())

secondword = message.split()

print(secondword[2]) # Output is equal to "name".

print(message.split("."))

# Join : It joins seperated expressions.

print(" ".join(secondword)) # join with space

print("*".join(secondword)) # join with *

print("-".join(secondword)) # join with -

# Find : It finds first index of word that you want.

print(message.find("Johnson")) # Output is 24.

# Startswith : It return true or false and  does control of letter in first index.If this letter is equal to parameter of startwith,startswith returns true If startswith hasn't this letter in the first index.It returns false.

print(message.startswith("H")) # false Because value of first index space.

# Endwith : It return true or false and  does control of letter in last index.If this letter is equal to parameter of endwith,endwith returns true If endwith hasn't this letter in the last index.It returns false.

print(message.endswith(".")) #true because value of last index is ".".

# Center : structure is like "center(number of character)".

print(message.center(100)) # Output is like combination of 50 space and message variable.

print(message.center(50,"*"))# Output is like combination of 50 * and message variable.





