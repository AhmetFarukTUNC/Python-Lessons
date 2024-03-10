class Math:
    def summation(self,number1,number2):
        return number1 + number2
    
    def substraction(self,number1,number2):
        return number1 - number2
    
    def multiplication(self,number1,number2):
        return number1 * number2
    
    def divide(self,number1,number2):
        return number1 / number2

math = Math()

print("Result is " + str(math.summation(2,78)))
