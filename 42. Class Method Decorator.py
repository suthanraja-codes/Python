class student:

    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count += 1

    def printDetails(self):
        print("The Name Is ",self.name," And The Age Is ",self.age)

    @classmethod
    def total(class_variable):
        return class_variable.count

o = student("suthan",21)
o.printDetails()
print(student.total())

a = student("king",20)
a.printDetails()
