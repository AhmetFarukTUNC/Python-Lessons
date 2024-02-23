# We defined a dictionary named as information.

information = {
    "name":"Understandable",

    "surname":"Economy",

    "birthPlace":"Ankara",

    "idNumber":141211111111111


}

print(type(information)) # We printed type of information.

print(information.keys()) # We printed keys of information dictionary as array.

print(information.values()) # We printed values of information dictionary as array.

print(information.items()) # We printed information dictionary.

print(information.get("name")) # We printed value of name key.

information.update({"Gender":"Male"}) # We changed "Gender" key as Erkek

print(information) # We printed information dictionary.

information2 =information.copy() #  We copied nformation dictionary and assigned to information2.

print(information2) # We printed information2.

print(information.__len__()) # We printed element number of information dictionary.

information.pop("idNumber") # We removed "idNumber" key from information dictionary together with his value.

print(information) # We printed information dictionary.

information.clear() # We removed all keys and values.

print(information) # We printed empty dictionary.