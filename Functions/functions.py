# We created a function named as listCredits.

def listCredits():

    # We created a list this list is containing "Fast Credit","Particular to paycheck from Jenniferbank","Happy retirement consumer loan".    
    credits = ["Fast Credit","Particular to paycheck from Jenniferbank","Happy retirement consumer loan"]

    # We printed elements of credits array bottom to bottom.

    for credit in credits:
       print(credit)

# We called to listCredits function a lot of times.

listCredits()

print()

listCredits()

print()

listCredits()

print()

listCredits()

# We creted a function named as hello and took visiter as parameter and parameter name is "name".We printed hello and space and visiter.

def hello(name = "visiter"):
    print("Hello " + name)

hello()

# We wrote a function that calculate of triangle area.

def calculateAreaOfTheTriangle(a,b):
    return a*b/2

# We called function and took 12 and 24 numbers as parameter and assigns to variable named as area.

area = calculateAreaOfTheTriangle(12,24)

# We printed returnedvalue of area 

print(area)