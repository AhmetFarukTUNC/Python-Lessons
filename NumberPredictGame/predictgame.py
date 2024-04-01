number = 25 # Number is equal to 25.

right = 10 # Right is equal to 10.

while right > 0:  # Loop until the number of guesses is greater than 0

    predict = int(input("Please input a positive number : "))  # Take user input

    if predict < 0:  # Check if the input is not positive
        print("Number that you entered is not positive.")
        continue  # Skip the rest of the loop and start over
    
    right -= 1  # Decrease the number of guesses by 1

    if number == predict:  # Check if the guess is correct
        print("You have made a correct prediction. Congratulations!")
        break  # End the loop if the guess is correct
    
    elif number > predict:  # Check if the guess is lower than the number
        if right != 0:  # Check if there are remaining guesses
            print("Up, {} guesses left.".format(right))  # Inform the user about remaining guesses

    else:  # If the guess is higher than the number
        if right != 0:  # Check if there are remaining guesses
            print("Down, {} guesses left.".format(right))  # Inform the user about remaining guesses

    if right == 0:  # Check if there are no remaining guesses
        print("You don't have any guesses left.")
