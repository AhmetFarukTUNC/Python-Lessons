# x = 10

# if x>5:
#     raise Exception("X 5'ten büyük olamaz.")

import re

def check_password(psw):

    if len(psw)<8:

        raise Exception("Parola en az 8 karakterden oluşmalıdır.")

    elif not re.search("[a-z]",psw):

        raise Exception("Parola küçük harf içermelidir.")
    
    elif not re.search("[A-Z]",psw):

        raise Exception("Parola büyük harf içermelidir.")
    
    elif not re.search("[0-9]",psw):

        raise Exception("Parola rakam içermelidir.")

    elif not re.search("[_@$]",psw):

        raise Exception("Parola alfa numeric karakter içermelidir.")
    
    elif re.search("\s",psw):

        raise Exception("Parola boşluk içermemelidir.")
    
psw = "123456789aA_"

try:

    check_password(psw)

except Exception as ex:

    print("Error :",ex)

else:

    print(psw)

finally:

    print("Şifre Kullanılabilir.")

class person:

    def __init__(self,name,year):

        if len(name)>10:

            raise Exception("Fazla karakter girdiniz.")
        
        else:

            self.name =name
            
person("Ahmet Faruk",2003)