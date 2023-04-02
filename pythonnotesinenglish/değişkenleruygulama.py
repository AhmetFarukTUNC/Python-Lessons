# Örnek 1 : Bir müşteri'nin aşağıdaki bilgileri için değişken oluşturunuz.

# Ad

# Soyad

# Cinsiyet

# Doğum Yılı

# Adres

# TC

# Yaş

# NOT : İnteger bir değerden string bir değeri çıkartamazsın.

customername="Ahmet Faruk"

customersurname="TUNÇ"

customergender="E"

customerbirthyear=2003

customeradress="Menekşe Mahallesi Sümbül Sokak No : 13 İzmir"

customeridentifynumber=52372313873

customerage=2023-customerbirthyear


# YAZDIRMA İŞLEMLERİ

print("Müşteri adı - soyadı : "+customername+customersurname)

print("Müşteri Cinsiyeti : "+customergender)

print("Müşteri Doğum Yılı :",customerbirthyear)

print("Müşteri Adresi : "+customeradress)

print("Müşteri TC :",customeridentifynumber)

print("Müşteri Yaşı :",customerage)


# Aşağıdaki siparişlerin hesap bilgisini hesaplayın.

# Sipariş1 = 110 TL

# Sipariş2 = 1100.50 TL

# Sipariş3 = 256.95 TL

# Bu değişkenleri topla ve ekrana yazdır.

firstorder =110 

secondorder=1100.50

thirdorder=256.95

totalprice=firstorder+secondorder+thirdorder

print("Your total price is",totalprice,"TL.")

# Sipariş1 değişkenini str yapma ve ekrana yazdırma

firstorder=str(firstorder)

print("Price of first order is {} in your shopping.".format(firstorder+" TL"))

# Tüm siparişlerileri string yapma ve ekrana yazdırma

print("Price of first order is {} in your shopping.".format(str(firstorder)+" TL"))

print("Price of second order is {} in your shopping.".format(str(secondorder)+" TL"))

print("Price of third order is {} in your shopping.".format(str(thirdorder)+" TL"))









