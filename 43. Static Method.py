
class student:
     
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printall(self):
        print("name ",self.name," and age is ",self.age)

    @staticmethod
    def welcome():
        print("Welcome To My Programs")

o = student("suthan",21)
o.printall()
o.welcome()