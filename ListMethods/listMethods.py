List1 = [1,2,5,"Hello",2.5] # Creating a list containing integers, a string, and a float 

List1.append("Understandable Economy") # We added "Understandable Economy" to List1.

print(List1) # We printed List1 array.

List1.insert(1,"I am Ahmet.") # We added "I am Ahmet." expression to second index of array named as List1.

print(List1) # We printed List1 array.

List1.remove(2) # We removed value of third index from List1 array.

print(List1) # We printed List1.

List1.pop() # Removing the last element from List1

print(List1) # Printing List1 after removing the last element

List2 = List1.copy() # Creating a copy of List1 named List2

print(List2) # Printing List2

numbers = [1,3,5,7,9] # Creating a list 'numbers' containing integers

letters = ["a","b","c","d","e","f"] # Creating a list 'letters' containing letters

numbers.extend(letters) # Extending 'numbers' list with elements from 'letters' list

newList = numbers # Assigning 'numbers' variable to 'newList'

print(newList) # Printing newList

print(numbers.count(3)) # Counting occurrences of '3' in 'numbers' list

# Sorting 'numbers2' list in reverse order
numbers2 = [4, 7, 5, 67, 90, 13, 45, 42]
numbers2.sort(reverse=True)
print(numbers2)

# Clearing the 'numbers' list
numbers.clear()
print(numbers)


cities = list(("Istanbul", "Ankara", "Çorum")) # Creating a list 'cities'

# Reversing the 'cities' list
cities.reverse()
print(cities)


cities2 = cities # Assigning 'cities' variable to 'cities2'


cities2[0] = "İzmir" # Modifying the first element of 'cities2' list


print(cities) # Printing 'cities' list after modification