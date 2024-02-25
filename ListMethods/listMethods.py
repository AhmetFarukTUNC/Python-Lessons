List1 = [1,2,5,"Hello",2.5]

List1.append("Understandable Economy")

print(List1)

List1.insert(1,"I am Ahmet.")

print(List1)

List1.remove(2)

print(List1)

List1.pop()

print(List1)

List2 = List1.copy()

print(List2)

numbers = [1,3,5,7,9]

letters = ["a","b","c","d","e","f"]

numbers.extend(letters)

newList = numbers

print(newList)

print(numbers.count(3))

numbers2 = [4,7,5,67,90,13,45,42]

numbers2.sort(reverse=True)

print(numbers2)

numbers.clear()

print(numbers)

cities = list(("Istanbul","Ankara","Çorum"))

cities.reverse()

print(cities)

cities2 = cities

cities2[0] = "İzmir"

print(cities)

# Array is referemce type.

