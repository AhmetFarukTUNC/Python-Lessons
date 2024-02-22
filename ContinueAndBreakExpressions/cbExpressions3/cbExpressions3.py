counter = 2 # counter is equal to 2

# This loop runs three times.

for i in range(0,3):

    # We took username from user
    
    username = input("Username : ")

    # We took password from user

    password = input("Password : ")

    # We defined default username.

    systemUsername = "Understandable Economy"

    # We defined default password.

    systemPassword = "123456"

    # If username is equal to default username and password is equal to default password,it is printed "Login is success,welcome" and it is exited from loop.

    if username == systemUsername and password == systemPassword:
        print("Login is success,welcome.")
        break

    # If username is not equal to default username and password is not equal to default password,counter is not equal to 0,it is printed "Incorrect login, please try again later.You have (value of counter) attempts left" and counter is decreased.

    elif (username != systemUsername or password != systemPassword) and counter != 0:
        print("Incorrect login, please try again later.You have {} attempts left".format(counter))

        counter -=1

    # Otherwise,it is printed "You have (value of counter) attempts left and exiting from system..."

    else:
        print("You have {} attempts left and exiting from system...".format(counter))