sayı = range(1,1001) # We assigned numbers from 1 to 1001 to the number variable.

# Then,If number is odd we printed (value of i) is double number.If number is single we printed (value of i) is single number.

for i in sayı:
    if i % 2 == 0:
        print("{} is double number.".format(i))

    elif i % 2 == 1:
        print("{} is single number.".format(i))