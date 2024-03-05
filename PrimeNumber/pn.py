number = int(input("Input number : "))

asalMi = "Yes"

for x in range(2,number):
    if(number%x == 0):
        asalMi="No"
        break

if asalMi =="Yes":
   print("This number is prime number.")
else:   
   print("Not prime number.")