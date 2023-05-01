# create set

# set is creating as {item1,item2,item3}

fruits={"orange","apple","banana"}

# print (fruits[0]) # you don't call any element.

for i in fruits:
    print(i)

"""

orange
apple
banana

""" 

# Set mothods

fruits.add("cherry") # It adds element to random a rea in set.

print(fruits) # Set can change {'apple', 'cherry', 'orange', 'banana'}.After that output can be different.

# Update split letter from word and adds as singular.

fruits.update("mango","grape")

print(fruits) # {'banana', 'r', 'e', 'm', 'apple', 'p', 'o', 'a', 'g', 'n', 'cherry', 'orange'} is output.

mylist=[1,2,5,4,4,2,1]

print(mylist) # [1, 2, 5, 4, 4, 2, 1]

print(set(mylist)) # {1, 2, 4, 5}

fruits.remove("orange") # Remove function removes specify a parameter.Parameter is "orange".

print(fruits) # {'e', 'apple', 'o', 'cherry', 'banana', 'r', 'n', 'a', 'p', 'g', 'm'}

fruits.discard("apple") # Discard function removes specify a parameter.Parameter is "apple".

print(fruits) # {'e', 'a', 'r', 'o', 'p', 'banana', 'cherry', 'n', 'm', 'g'}

fruits.pop() # Pop function deletes last element in normal condition but if we have a set ,this function deletes any element.

print(fruits) # Output is {'m', 'a', 'g', 'e', 'banana', 'cherry', 'n', 'o', 'r'} but this output can be different.

fruits.clear() # Clear function deletes all elment of set.

print(fruits) # Output is set().


