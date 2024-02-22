username = "Understandable Economyy"

password = "12345678"

if username == "Understandable Economy" and password == "1234567":
    print("Login is success,welcome")

elif not(username == "Understandable Economy") and password == "1234567":
    print("Username is wrong")

elif not(password == "1234567") and username == "Understandable Economy":
    print("Password is wrong.")

else : 
    print("Username and password is wrong.")

dolarYesterday = 31.

dolarToday = 31.75

if dolarYesterday < dolarToday:
    print("increasing arrow")

elif dolarYesterday > dolarToday:
    print("decreasing arrow")

else:
    print("equal arrow")

print("finished")