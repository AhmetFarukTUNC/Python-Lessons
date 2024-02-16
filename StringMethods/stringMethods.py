x = "Great Live"

y = x.lower()

print(y)

z = x.upper()

print(z)

print(z.islower())

print(x.isupper())

print(x.isnumeric())

a = "2134"

print(a.isnumeric())

print(x.isalnum())

print(x.capitalize()) # ilk harfi büyük yapar.

print(x.title()) # Her kelimenin ilk harfini büyük yapar.

print(x.swapcase()) # büyük harfleri küçük harf,küçük harfleri büyük harf yapar.

print(x.count("o"))

b = "  Hello  "

print(b)

print(b.strip(" ")) # Baştaki ve sondaki verilen parametreye uygun değeri siler.

print(b.lstrip(" ")) # Baştan parametreye uygun olan değerleri siler.

sentence = "I am Ahmet.I am twenty years old."

print(sentence.split(" "))

sentenceaslist = sentence.split(" ")

print(" ".join(sentenceaslist))

print("**".join(sentenceaslist))

print(sentence.find("tw"))

print(sentence.replace("twenty","21"))

name = "Understandable"

surname = "Economy"

mission = "Teach"

informations  = [name,surname,mission]

print(type(informations))

print("Person Name : {} Person Surname : {} Person Mission : {}".format(informations[0],informations[1],informations[2]))
