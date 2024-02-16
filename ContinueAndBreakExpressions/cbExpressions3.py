counter = 2

for i in range(0,3):
    
    username = input("Username : ")

    password = input("Password : ")

    systemUsername = "Understandable Economy"

    systemPassword = "123456"

    if username == systemUsername and password == systemPassword:
        print("Login is success,welcome.")
        break
    elif (username != systemUsername or password != systemPassword) and counter != 0:
        print("Incorrect login, please try again later.You have {} attempts left".format(counter))

        counter -=1

    else:
        print("You have {} attempts left and exiting from system...".format(counter))