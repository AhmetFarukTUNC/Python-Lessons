number = 25

right = 10

while right > 0:

    predict = int(input("Please input a positive number : "))

    if predict < 0:
        print("Number that you entry is not positive.")
        continue
    
    right -= 1

    if number == predict:
          print("You have a correct predict.Congratulations!")
          break
    
    elif number > predict:
         if right != 0:
            print("Up,{} left.".format(right))

    else:
         if right != 0:
              print("Down,{} left.".format(right))

    if right == 0:
         print("You don't have right anymore.")
    
