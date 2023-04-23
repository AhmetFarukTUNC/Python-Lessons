# Square a number with map

def square1(number):
    return number**2

numbers=[1,3,5,7]

numbers=list(map(square1,numbers)) # numbers = [1,9,25,49]

print(numbers) # [1,9,25,49]

for i in numbers:
    print(i) 

"""
output:
1
9
25
49
"""

# Square a number with map and lambda

numbers=list(map(lambda number:number**2,numbers)) # numbers = [1,81,625,2401]

print(numbers) # [1,9,625,2401]

for i in numbers:
    print(i) 



"""
output:
1
9
625
2401
"""

# Check uniqueness of number with filter and lambda and print it to the screen

def singularnumber(number):

    return number%2!=0

numbers2=[1,2,3,4,5,6,7,8,9,10]

list2=list(filter(singularnumber,numbers2)) # list2 = [1,3,5,7,9]

print(list2) # [1,3,5,7,9]

# Check the double of the number with filter and lambda and print it to the screen

list2=list(filter(lambda number3:number3%2==0,numbers2)) # list2 = [2,4,6,8,10]

print(list2) # [2,4,6,8,10]

