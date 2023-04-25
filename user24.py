class User:
    # krishna = 0
    def __init__(self, user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd
    def register(self):
        print("registering ")

    def loggin(self):
        print("Loging In ")

    def greet(self):
        print("king")

class Student(User):
    def greet(self):
        print("helloi krishna"+self.user_name)
    def greet_1(self):
        print("hello")

class Teacher(User):
    def __init__(self,Name,Fees,user_name,pwd):
        super().__init__(self,user_name,pwd)
        self.Fees=Fees
        self.Name = Name
    def greet(self):
        super().greet()
        print("i am teacher")

class multi(Student,Teacher):
    def greet_user(self):
        print("hello")
