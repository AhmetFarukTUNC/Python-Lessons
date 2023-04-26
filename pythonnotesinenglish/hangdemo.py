#Print numbers in list

list = ["1","2","5a","10b","abc","10","50"]


for i in list:
    
    try:
        i = int(i)
     
    except ValueError:
       
       pass

    else:

        print(i)

# Generally example about errors

while True:

    number = input("Number : ")

    if number=="q":

        break

    try :

        number = float(number)

        print(number)

    except ValueError:

        print("Invalid number.")

        continue
        
# Has it turkish character?

while True:

    turkishcharacter = "şçğüöıİ"

    parola = input("Parola : ")
    if parola =="q":

        break

    for i in parola:

        if i in turkishcharacter:

            raise TypeError("Türk karakter giremezsin.")
    else:

        print("Geçerli parola")

        break

# Error messages with factorial function

def factorial(x):

    

    if x==0 :
        raise ValueError("X 0'dan büyük olmalıdır.")
    
    result =1
    
    for i in range(1,x+1,1):
        result*=i
    print(result)
    
x=int(input(" X : "))  

factorial(x)


    

    

    

