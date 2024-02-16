name = str(input("Please,input your name : "))

age = int(input("Please,input your age : "))

educationState = str(input("Please,input your education state : "))

educationStates = ("primary school","middle school","high school","university")

if educationState not in educationStates:
    print("Please,Input a valid education state")

elif (age >= 18) and (educationState == "high school" or educationState == "university"):
    print("driving license requirements have been passed") 

else:
    print("Driving license requirements do not match")

