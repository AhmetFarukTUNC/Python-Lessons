class Math:

    def __init__(self,number1,number2):
        self.number1 = number1

        self.number2 = number2


    def summation(self):
        return self.number1 + self.number2
    
    def substraction(self):
        return self.number1 - self.number2
    
    def multiplication(self):
        return self.number1 * self.number2
    
    def divide(self):
        return self.number1 / self.number2

math = Math(23,45)

print("Result is " + str(math.summation()))

print("Result is " + str(math.substraction()))

print("Result is " + str(math.multiplication()))

print("Result is " + str(math.divide()))