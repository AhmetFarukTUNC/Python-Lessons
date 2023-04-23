def list(newlist):

    newlist[0]="İstanbul"
    return newlist

list1=["Ankara","Kocaeli"]

list=list(list1)

print(list)

list2=["Ankara","Kocaeli"]

n = list2[:]

n[0] = "İstanbul"

print(n)

print(list2)

def summary(a=10,b=20,c=30):

    return a+b+c

print(summary(20,30,40))

def add(*params):

    return sum((params))

print(add(10,20,30,40,50,89))

def add2(*params,total=0):
    for i in params:
        total+=i
    return total

print(add2(10,20,30,40,50,89))

def displayuser(**params):

    print(type(params))

    for key,value in params.items():

        print("{} is {}".format(key,value))

displayuser(name="John",surname="Kenedy",age=3)

displayuser(name="Abraham",surname="Lincoln",age=3)

displayuser(name="Brad",surname="Pitt",age=3)

def displayuser(**args):

    print(type(args))

    for key,value in args.items():

        print("{} is {}".format(key,value))

displayuser(name="John",surname="Kenedy",age=3)

displayuser(name="Abraham",surname="Lincoln",age=3)

displayuser(name="Brad",surname="Pitt",age=3)

def myfunction(a,b,c, *args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myfunction(10,20,30,40,50,60,70,Value1 = "Hello" , Value2 = "World!")

