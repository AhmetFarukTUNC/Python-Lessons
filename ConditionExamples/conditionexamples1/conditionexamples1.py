username = input("Please,Input your username : ") # We took username from user.

password = input("Please,input your password : ") # We took password from user.

systemusername = "Understandable Economy" # We defined default username.

systempassword= "123456" # We defined default password.

# If username is equal to defined username and password is equal to defined password,it prints to screen hello after that prints value of defined username,finally prints welcome.They are side by side.

if username == systemusername and password == systempassword:
    print("Hello {},welcome!".format(systemusername))

# If username and password is not equal to defined username and password,it prints Hello,username and password are wrong.

elif username != systemusername and password != systempassword:
    print("Hello,username and password are wrong.")

# If username is equal to defined username,it prints to "Hello,username is wrong".

elif username != systemusername:
    print("Hello,username is wrong.")

# If password is not equal to defined password,it prints hello,after that,prints defined username,finally,prints "password is wrong.".They are side by side.

elif password != systempassword:
    print("Hello {},password is wrong.".format(systemusername))

