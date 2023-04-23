class animal():
    # init is specify function.We use for contructor operation.

    def __init__(self,name,number):

        self.name = name
        
        self.number = number

        print("We created init function.")

    #   str is specify function.We use for wr,te string expression.

    def __str__(self):

        return "Created string method."

    def __len__(self):

        return f"{self.name} is {self.number} as number."
    
    def __del__(self):

        return f"{self.name} deleted."
    
a1=animal("Dog",5) # It prints "We created init function".

print(a1.__str__()) # Created string method.

print(a1.__len__()) # Dog is 5 as number.

print(a1.__del__()) # Dog deleted.

a2=animal("Cat",10) # It prints "We created init function".

print(a2.__str__()) # Created string method.

print(a2.__len__()) # Cat is 10 as number.

print(a2.__del__()) # Cat deleted.