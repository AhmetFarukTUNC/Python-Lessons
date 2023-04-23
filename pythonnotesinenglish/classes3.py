class person():
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

class teacher(person):
    def __init__(self,firstname,lastname,branch):
        super().__init__(firstname,lastname)
        self.branch=branch
    def whoamI(self):
        print(f"Hello!I am {self.firstname} {self.lastname} My branch is {self.branch}")

t1=teacher("Mustafa","Yılmaz",19)

t1.whoamI()