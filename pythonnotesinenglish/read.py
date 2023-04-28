# file=open("file4.txt","a",encoding="utf-8")

# file.write("Hello!\n")

# file.write("I!\n")

# file.write("am!\n")

# file.write("John!\n")

# file.close()

# file = open("file4.txt","r",encoding="utf-8")



# for i in file:
#     print(i)

# Read function is reading document.

# content=file.read(6)

# content2=file.read(3)

# content3=file.read(4)

# content4=file.read(7)

# print(content) # Hello!

# print(content2) # I!

# print(content3) # am!

# print(content4) # John!

# print(file.read()) Output is in bottom.

"""
Hello!
I!
am!
John!

"""

# Readline function reading a line of document.

# print(file.readline()) # Hello!

# print(file.readline()) # I!

# print(file.readline()) # am!

# print(file.readline()) # John!

# It takes to list data of document.

# print(file.readlines()) # ['Hello!\n', 'I!\n', 'am!\n', 'John!\n']

# filecontent=file.readlines()

# print(filecontent[0]) # Hello!

# print(filecontent[1]) # I!

# print(filecontent[2]) # am!

# print(filecontent[3]) # John!

# file.close()