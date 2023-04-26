# Take student information

name = input("Name : ")

surname = input("Surname : ")

number = int(input("Student Number : "))

phone = int(input("Phone : "))

# Create a dictionary

students =dict()

# Add student informations to student dictionary.

students = {
    "name":name,
    "surname":surname,
    "number":number,
    "Phone":phone
}

# Print to screen dictionary.

print(students)

# Print to screen the student information.

print("name : ",students["name"])
print("surname : ",students["surname"])
print("student number : ",students["number"])
print("phone : ",students["Phone"])

