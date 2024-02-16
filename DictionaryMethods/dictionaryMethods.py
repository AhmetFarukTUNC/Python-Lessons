information = {
    "name":"Understandable",

    "surname":"Economy",

    "birthPlace":"Ankara",

    "idNumber":141211111111111


}

print(type(information))

print(information.keys())

print(information.values())

print(information.items())

print(information.get("name"))

information.update({"Gender":"Erkek"})

print(information)

information2 =information.copy()

print(information2)

print(information.__len__())

information.pop("idNumber")

print(information)

information.clear()

print(information)