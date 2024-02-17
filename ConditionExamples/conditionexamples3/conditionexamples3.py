name = str(input("Please,input your name : ")) # I took name from user

age = int(input("Please,input your age : ")) # I took age from user

educationState = str(input("Please,input your education state : ")) # I took education state from user 

educationStates = ("primary school","middle school","high school","university") # I added options for education state.

# If education state is not in educationState(educationStates = ("primary school","middle school","high school","university")),it prints "Please,Input a valid education state".

if educationState not in educationStates:
    print("Please,Input a valid education state")

# If education state is high school or university and age is great equal than 18,it prints "driving license requirements have been passed".

elif (age >= 18) and (educationState == "high school" or educationState == "university"):
    print("driving license requirements have been passed") 

# Otherwise,it prints "Driving license requirements do not match"

else:
    print("Driving license requirements do not match")

