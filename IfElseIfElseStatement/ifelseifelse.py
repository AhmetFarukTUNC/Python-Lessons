username = "Understandable Economyy" # username is equal to "Understandable Economyy" 

password = "12345678" # password is equal to 12345678.

# If username is Understandable Economy and password is 1234567,then,It is printed expression that Login is success,welcome

if username == "Understandable Economy" and password == "1234567":
    print("Login is success,welcome")

# If username is not Understandable Economy and password is 1234567,then,It is printed expression that username is wrong.

elif not(username == "Understandable Economy") and password == "1234567":
    print("Username is wrong")

# If username is Understandable Economy and password is not 1234567,then,It is printed expression that password is wrong.

elif not(password == "1234567") and username == "Understandable Economy":
    print("Password is wrong.")

# Otherwise,It is printed expression that username and password is wrong.

else : 
    print("Username and password is wrong.")

dolarYesterday = 31.23 # dolarYesterday is equal to 31.23. 

dolarToday = 31.75 # dolarToday is equal to 31.75.

# If dolarYesterday is lesser than dolarToday,then,it is printed expression that increasing arrow.

if dolarYesterday < dolarToday:
    print("increasing arrow")

# If dolarYesterday is greater than dolarToday,then,it is printed expression that decreasing arrow.

elif dolarYesterday > dolarToday:
    print("decreasing arrow")

#Otherwise,it is printed expression that equal arrow.

else:
    print("equal arrow")

print("finished") # It is printed expression that finished.