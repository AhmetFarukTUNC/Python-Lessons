# İnstance is equal to object.

# Define a class and create a lot of object with class.

class person():

    address = "No İnformation"

    # class attributes

    # object attributes
    #    constructor

    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("Constructor method runs.")
    # methods
    def intro(self):
        print(f"Hello Mr. {self.name}")

    def calculate(self):
        return 2023-self.year


p1=person("Ali",1990) # p1 object

p2=person("Yağmur",1995) # p2 object

# Update operations

p1.address="bringston street"

print(f"{p1.name} - {p1.year} - {p1.address}")

print(f"{p2.name} - {p2.year} - {p2.address}")

print(p1)

print(p2)

print(type(p1))

print(type(p2))

# call method

p1.intro()

p2.intro()

print(p1.calculate())

print(p2.calculate())