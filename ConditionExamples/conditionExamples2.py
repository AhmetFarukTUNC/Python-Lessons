print("Hello,Welcome to Body Mass App...")

size = int(input("Please,Input your size as centimeter : "))

kilo = int(input("Please,Input your kilo as kilogram : "))

index = round(((kilo)/(size/100)**2),2)

if index <= 18.5:
    print("Your body mass index is {}'dır.You are in the underweight group.".format(index))

elif index > 18.5 and index <= 24.9:
    print("Your body mass index is {}'dir.You are in the normal weight group.".format(index))

elif index > 25 and index <= 29.9:
    print("Your body mass index is {}'dir.You are in the overweight group.".format(index))

elif index > 30 and index <= 40:
    print("Your body mass index is {}'dir.You are in the obese group.".format(index))

elif index > 40:
    print("Your body mass index is {}'dir.You are in the extremely obese group.".format(index))