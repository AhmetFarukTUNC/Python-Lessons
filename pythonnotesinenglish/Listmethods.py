# min is returning minimum value 

list = [1,10,5,16,4,9,10]

letters = ["a","g","s","b","y","a","s"]

value=min(list)

print(value) #1

value2 = max(list)

print(value2) #16

value3 = min(letters)

value4 = max(letters)

print(value3) # a

print(value4) # y

# Update list

list[4] = 40

print(list) # [1, 10, 5, 16, 40, 9, 10]

# Append is adding elemnet to end in list

list.append(49)

print(list) # [1, 10, 5, 16, 40, 9, 10, 49]

# Insert is adding to specify index the element.

list.insert(1,38)

print(list) # [1, 38, 10, 5, 16, 40, 9, 10, 49]

list.insert(-1,52) 

print(list) # [1, 38, 10, 5, 16, 40, 9, 10, 52, 49]

# If pop has not parameter,pop is deleting last element.

list.pop(0) # We are deleting element in 0. index.

print(list) # [38, 10, 5, 16, 40, 9, 10, 52, 49].

list.pop(-1)# We are deleting element in -1. index.

print(list) # [38, 10, 5, 16, 40, 9, 10, 52]

# Remove function is removing any element.(We indicates this element with parameter.)

list.remove(38) # This row is removing 38 number from list.

print(list) # [10, 5, 16, 40, 9, 10, 52]

# Sort function  is sorting normally the list.

list.sort()

print(list) # [5, 9, 10, 10, 16, 40, 52]

letters.sort()

print(letters) # ['a', 'a', 'b', 'g', 's', 's', 'y']

# Reverse function is sorting reverse the list.

list.reverse()

print(list) # [52, 40, 16, 10, 10, 9, 5]

letters.reverse()

print(letters) # ['y', 's', 's', 'g', 'b', 'a', 'a']

print(len(list)) # Output is 7.

print(len(letters)) # Output is 7.

# Count function is counting how many.

print(list.count(10)) # Output is 2.

print(letters.count("a")) # Output is 2.

# Clear function is clearing all list.

list.clear()

print(list) # Output is empty list.([])















