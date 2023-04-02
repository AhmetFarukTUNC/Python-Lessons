#This lesson will be full with example.

#First Example is about differences between "" and ''.

firstname="Ahmet"
Secondname='Ahmet'
firstsurname="Tunç"
secondsurname='Tunç'

print(firstname + " " + firstsurname)

# The second example is about printing the value of 3 variables in a row.

name=" Mehmet"
surname=" Yılmaz."
text="My name is "
print(text + name + surname)  

# Third example is about  error of collect of variables in the str and int data type.

name2="Burak"
surname2="Güngör"
age =36
print(f"My name is {name2} {surname2}.I am {age} years old.")
print("My name is {} {}.I am {} years old".format(name2,surname2,age))
# print("My name is " + name2 + " " + surname2 + ".I am " + age + " years old.")

#Fourth example is about pass to bottom row.We are using \n for do this.

name3="Mehmet"
surname3="Şahin"
age=36
print("My name is " + name3 + " " + surname3 + ".\nI am " + str(age) +" years old.")

# Fifth example is about find everthing index of string expression and print this expression.

name4 = "Murat"
surname4 = "Yılmaz"
age = 36
greeting = name4 + surname4 + str(age)
print(greeting)
print(greeting[0])
print(greeting[3])
print(greeting[len(greeting)-1])

# This episode is about generally example.

# First example

name5 = "Furkan"

surname5 = "Turan"

age = 36

greeting = "My name is " + name + surname + ".I am  " + str(age) +" years old."

length = len(greeting)

print(greeting)

print(length-1)

print(greeting[-1])

print(greeting[2:5])

print(greeting[3:])

print(greeting[:15])

print(greeting[2:40:3])






