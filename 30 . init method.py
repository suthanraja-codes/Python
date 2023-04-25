# __init__ method is a constructor

class student:
    def __init__(self, name):
        print("call me when instance created")
        self.name = name

    def printall(self):
        print("Name : ", self.name)


obj = student('suthan')
obj2 = student("king")
obj.printall()

print(obj.__dict__)

print(obj2.__dict__)

print(student.__dict__)
