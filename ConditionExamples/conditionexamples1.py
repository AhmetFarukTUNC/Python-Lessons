username = input("Please,Input your username : ")

password = input("Please,input your password : ")

systemusername = "Understandable Economy"

systempassword= "123456"

if username ==systemusername and password == systempassword:
    print("Hello {},welcome!".format(systemusername))

elif username != systemusername and password != systempassword:
    print("Hello,username and password are wrong.")

elif username != systemusername:
    print("Hello,username is wrong.")

elif password != systempassword:
    print("Hello {},password is wrong.".format(systemusername))

