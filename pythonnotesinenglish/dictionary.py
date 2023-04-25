# Dictionary is running in key-value format.

# Create two lists as contries and licence plates and print to screen Kocaeli Licence plate.Kocaeli Licence plate is 41.

countries = ["Kocaeli","Istanbul"]

licenceplate = [41,34]

print(licenceplate[countries.index("Kocaeli")]) # 41

print(licenceplate[countries.index("Istanbul")]) # 34

# Create a dictionary

licenceplatedict = {"Kocaeli":41,"Istanbul":34}

print(licenceplatedict["Kocaeli"]) # 41

print(licenceplatedict["Istanbul"]) # 34

licenceplatedict["Ankara"]=6

print(licenceplatedict) # {'Kocaeli': 41, 'Istanbul': 34, 'Ankara': 6}

# Create user dictionary and add two person and print information to screen.

users = {
   "John Wick" : {

    "Age":36,

    "E - Mail":"johnwick@gmail.com",

    "Address":"U.S.A",

    "Phone":123456

   },

   "John Kenny" : {

   "Age":38,

   "E - Mail":"Johnkenny@gmail.com",

   "Address":"England",

   "Phone":789101112131415,

   "Role":["Admin","User"]
   }

}

print(users["John Kenny"]) # {'Age': 38, 'E - Mail': 'Johnkenny@gmail.com', 'Address': 'England', 'Phone': 789101112131415, 'Role': ['Admin', 'User']}

print(users["John Wick"]) # {'Age': 36, 'E - Mail': 'johnwick@gmail.com', 'Address': 'U.S.A', 'Phone': 123456}

print(users["John Kenny"]["Age"]) # 38

print(users["John Kenny"]["E - Mail"]) # Johnkenny@gmail.com

print(users["John Kenny"]["Address"]) # England

print(users["John Kenny"]["Role"][0]) # Admin

# Lesson finished


