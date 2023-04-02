# DEĞİŞKENLER TANIMI 

# Değişken Tanımlama Kuralları

# Değişkenler rakam ile başlamaz.

1number=10

# Pythonda büyük harf küçük harf duyarlılığı vardır.

age=20

Age=30

print(age)

print(Age)

# Değişkenler ile alakalı 1 tane örnek

firstnumber=20

secondnumber=30

print(firstnumber)

print(secondnumber)

firstnumber+=30

print(firstnumber)

# Türkçe karakter kullanılmaz.Ama lullanırsanız da hata vermez.

yaş=10

yas2=20

_yas3=30

print(yaş)

print(yas2)

print(_yas3)

# Veri tipleri

x=1 # Veri tipi = int

x=2.5 #Veri tipi = float

name1="Furkan"

name2='Furkan'

print(name1)

print(name2)

isstudent=True # Veri tipi : bool

print(isstudent)

# Değişkenler hakkında ufak bir örnek

a=20

b=30

print(a+b) #50

# Değişkenler hakkında ufak bir örnek(String Toplama).

x="20"

y="30"

print(x+y) #2030

# Değişkenler hakkında ufak bir örnek(Ad - Soyad Hakkında Ufak Bir Örnek)

firstname = "Ahmet Faruk"
lastname = " TUNÇ"
print(firstname+lastname) #Ahmet Faruk TUNÇ

# Tek bir satırda birden fazla değişkeni tanımlama

z,t,name,isstudent=(60,75,"Mehmet",False)

print(z) # 60

print(t) # 75

print(name) # Mehmet

print(isstudent) # False

# Vergi oranı %27 olan bir ürünün total fiyatını hesaplayınız.(Ürünün fiyatı = 10000 TL)

oran=27/100

fiyat=10000

totalfiyat=fiyat+fiyat*oran

print("Produce price is",totalfiyat)
