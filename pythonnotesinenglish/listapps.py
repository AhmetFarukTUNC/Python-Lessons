names=["Ali","Yağmur","Hakan","Deniz"]

years=[1998,2000,1988,1987]

# add to end of list cenk string expression.

names.append("Cenk")

print(names) # ['Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

# Add to top of list Sena name.

names.insert(0,"Sena")

print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

# Remove from list deniz name.

names.remove("Deniz")

print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Cenk']

# What is index of deniz name?

print(names.index("Hakan")) # 3

# Is Ali in list?

print("Ali" in names) # True

# Reverse list elements.

names.reverse()

print(names) # ['Cenk', 'Hakan', 'Yağmur', 'Ali', 'Sena']

# Sort as alphabet lsit elements.

names.sort()

print(names) # ['Ali', 'Cenk', 'Hakan', 'Sena', 'Yağmur']

# Sort small to big number years list.

years.sort()

print(years) # [1987, 1988, 1998, 2000]

# Convert to list Hello word sentence.

str = "hello world"

print(str.split(" ")) # ['hello', 'world']

# What is min and max element of years list?

print(min(years)) # 1987

print(max(years)) # 2000

# How many 1998 number in years list?

print(years.count(1998)) # 1

# Clear all elements of years list.

years.clear()

print([]) # []

# Store 3 company information in a list.

companies = []

c1=input("Company 1 : ")

c2=input("Company 2 : ")

c3=input("Company 3 : ")

companies.append(c1)

companies.append(c2)

companies.append(c3)

print(companies) # [value of c1,value of c2,value of c3]