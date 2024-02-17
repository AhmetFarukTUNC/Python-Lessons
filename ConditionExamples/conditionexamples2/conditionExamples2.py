print("Hello,Welcome to Body Mass App...") # It prints to screen "Hello,Welcome to Body Mass App..."

size = int(input("Please,Input your size as centimeter : ")) # We took height from user.

kilo = int(input("Please,Input your kilo as kilogram : ")) # We took kilo from user.

index = round(((kilo)/(size/100)**2),2) # We found body mass index.

# If index is lesser or equal to 18.5,it prints "Your body index is",after that 'value of index',finally,
# You are in the underweight group."

if index <= 18.5:
    print("Your body mass index is {}.You are in the underweight group.".format(index))

# If index is 18.5 between 24.9 and equal to 24.9 ,it prints "Your body index is",after that 'value of 
# index',finally,You are in the normal weight group."

elif index > 18.5 and index <= 24.9:
    print("Your body mass index is {}.You are in the normal weight group.".format(index))

# If index is 25 between 29.9 and equal to 29.9,it prints "Your body index is",after that 'value of index',finally,You are in the overweight group."

elif index > 25 and index <= 29.9:
    print("Your body mass index is {}.You are in the overweight group.".format(index))

# If index is 30 between 40 and equal to 40,it prints "Your body index is",after that 'value of index',
# finally,You are in the obese group."

elif index > 30 and index <= 40:
    print("Your body mass index is {}.You are in the obese group.".format(index))

# If index is greater than 40,it prints "Your body index is",after that 'value of index',finally,You are in the extremely obese group."

elif index > 40:
    print("Your body mass index is {}.You are in the extremely obese group.".format(index))