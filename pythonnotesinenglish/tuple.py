# What was list?

list1 = [1,2,3]

#What is the tuple?

tuple1 = (1,"iki",3)

# Print type of a variable to screen

print(type(list1)) # <class 'list'>

print(type(tuple1)) # <class 'tuple'>

# Find index of any data

print(list1[1]) # 2

print(tuple1[2]) # 3

# Find length of data structure and print to screen 

print(len(list1)) # 3

print(len(tuple1)) # 3

# Last generally example

list2 = [4,5,6]

tuple2 = (7,"sekiz",9)

print(list2) # [4, 5, 6]

print(tuple2) # (7, 'sekiz', 9)

list2[0] = "dört"

print(list2) # ['dört', 5, 6]

print(tuple2.count("sekiz")) # It has 1 sekiz so output is 1.

print(tuple2.index("sekiz")) #İndex of sekiz element is 1 so output is 1.

# numbers = list2 + tuple2

# print(numbers) # ERROR : You don't combination list and tuple.



