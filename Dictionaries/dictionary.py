# We defined dictionary that create from name and surname,age,birthday place attributes and assigns to Identify variable.

Identity = {
    "name":"Ahmet Faruk",
    "surname":"TUNÇ",
    "Age":21,
    "birthdayPlace":"Kütahya"
}

# We printed Identity variable.

print(Identity)

# We printed value of name attribute in Identity dictionary.

print(Identity["name"])

# We printed value of surnmae attribute in Identity dictionary.

print(Identity["surname"])

# We printed value of Age attribute in dictionary named Identity.

print(Identity["Age"])

# We printed value of birthPlace attribute in dictionary named Identity.

print(Identity["birthdayPlace"])

# We changed value of name attribute as Mehmet Faruk in dictionary named Identity.

Identity["name"] = "Mehmet Faruk"

# We printed changed Identity dictionary.

print(Identity)

# We changed value of identityNumber attribute as 12345678908 in dictionary named Identity 

Identity["identifyNumber"] =12345678908

# We printed value of identityNumber attribute in dictionary named Identity.

print(Identity["identifyNumber"])

# There is a dictionary named users.It has 2 element.There are first dictionary named AhmetCan and second dictionary named ArzuCan.Dictionary named AhmetCan has 4 attributes.Those is IdentityNumber,BirthayPlace and Age.This attributes values are 12345678909,Ankara,24 and 56675789879,Istanbul,29 for ArzuCan with order.

users = {"AhmetCan":{
    "IdentityNumber":12345678909,
    "BirthPlace":"Ankara",
    "Age":24
},

"ArzuCan":{
    "IdentityNumber":56675789879,
    "BirthPlace":"Istanbul",
    "Age":29
}

}

# We printed users dictionary.

print(users)