sayı = range(1,1001)

for i in sayı:
    if i % 2 == 0:
        print("{} is double number.".format(i))

    elif i % 2 == 1:
        print("{} is single number.".format(i))