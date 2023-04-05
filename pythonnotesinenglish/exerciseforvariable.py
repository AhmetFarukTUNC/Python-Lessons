# Example 1: Create a variable for the following information of a customer.

# Name

#Surname

#Gender

# Birthyear

# Address

#Id

#Age

# Note: You cannot extract a string value from an integer value.

customername="John"

customersurname="KENNEDY"

customergender="E"

customerbirthyear=2003

customeradress="Menekşe Mahallesi Sümbül Sokak No : 13 İzmir"

customeridentifynumber=52372313873

customerage=2023-customerbirthyear


# YAZDIRMA İŞLEMLERİ

print("Customer name - surname : "+customername+customersurname)

print("Customer gender : "+customergender)

print("Customer Birth Year :",customerbirthyear)

print("Custom Adress : "+customeradress)

print("Customer Id :",customeridentifynumber)

print("Customer Age :",customerage)


# Calculate the account information of the following orders.

# Order1 = 110 TL

# Order2 = 1100.50 TL

# Order3 = 256.95 TL

# Collect these variables and print them to the screen.

firstorder =110 

secondorder=1100.50

thirdorder=256.95

totalprice=firstorder+secondorder+thirdorder

print("Your total price is",totalprice,"TL.")

# Make order1 variable str and print it to the screen.

firstorder=str(firstorder)

print("Price of first order is {} in your shopping.".format(firstorder+" TL"))

# String all orders and print them to the screen.

print("Price of first order is {} in your shopping.".format(str(firstorder)+" TL"))

print("Price of second order is {} in your shopping.".format(str(secondorder)+" TL"))

print("Price of third order is {} in your shopping.".format(str(thirdorder)+" TL"))
