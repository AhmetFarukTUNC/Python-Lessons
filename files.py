# Open function uses for create and open document.

# This function has two parameters.Those is file name and file access mode.

# File access mode specifies the reason why the document was opened.

# Open document w parameter / w is printing once.After that, It deletes text when you are write new text.

newfile = open("Hello.txt","w",encoding="utf-8") # encoding="utf-8" is for turkish character.

newfile.write("Hello!") # It prints "Hello" expressiion to document.

newfile.close() # It closes document.It is necessary for security.


print(newfile) # <_io.TextIOWrapper name='Hello.txt' mode='w' encoding='cp1254'> is document information.

# Append method(a): w is printing once.After that, It doesn't delete text when you are write new text.

file2=open("world.txt","a")

file2.write("Hello ")

file2.write("World!")

file2.write("\nI am john.")

file2.close()

# Open document with create(x) method

open("file3.txt","x") # It creates file3 document.

open("world.txt","x") # It gives error.

